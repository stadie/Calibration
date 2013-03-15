# $Id: runTreeMaker_cff.py,v 1.11 2013/03/15 14:32:11 kirschen Exp $

import FWCore.ParameterSet.Config as cms
import os
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes


def runTreeMaker(
    process,
    isData=True,
    globalTag="",
    treeName="",
    writePhotons=False,
    hltSelection=[],
    reportEveryEvt=5000,
    testFileName="",
    numProcessedEvt=100
    ):


    # ---- Configuration ----------------------------------------------------------
    process.load('Configuration.EventContent.EventContent_cff')
    process.load('Configuration.StandardSequences.MagneticField_38T_cff')
    process.load('Configuration.StandardSequences.Reconstruction_cff')
    process.load('Configuration.StandardSequences.EndOfProcess_cff')
    process.load('Configuration.StandardSequences.GeometryDB_cff')
    process.load('Configuration.StandardSequences.Services_cff')
    process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
    process.GlobalTag.globaltag = globalTag

    process.load('JetMETCorrections.Configuration.DefaultJEC_cff')
    process.load('RecoBTag.Configuration.RecoBTag_cff')

    process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
    process.load('SimGeneral.MixingModule.mixNoPU_cfi')



    # ---- Message logger ---------------------------------------------------------
    process.load('FWCore.MessageService.MessageLogger_cfi')
    process.load("FWCore.MessageLogger.MessageLogger_cfi")
    process.MessageLogger.cerr.threshold             = 'INFO'
    process.MessageLogger.cerr.FwkReport.reportEvery = reportEveryEvt



    # ---- Input ------------------------------------------------------------------
    process.source = cms.Source(
        "PoolSource",
        fileNames = cms.untracked.vstring(testFileName)	
        )
    process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(numProcessedEvt)
        )
    process.options = cms.untracked.PSet(
        SkipEvent = cms.untracked.vstring('ProductNotFound'),
        Rethrow = cms.untracked.vstring('ProductNotFound'),
        wantSummary = cms.untracked.bool(True)
        )


    
    # ---- Filters ----------------------------------------------------------------
    # HLT
    process.load('HLTrigger.HLTfilters.hltHighLevel_cfi')
    process.hltHighLevel.HLTPaths = cms.vstring(hltSelection)
    process.hltHighLevel.andOr = cms.bool(True)
    process.hltHighLevel.throw = cms.bool(False)

    # standard filter sequence + ecal dead-cell tagger
    process.load('Calibration.CalibTreeMaker.cleaningSequences_cff')

#    ## New HO mis-reco Filter ____________________________________________________||
#    from SandBox.Skims.caloVsPFMetFilter_cfi import caloVsPFMetFilter
#    process.RA2CaloVsPFMETFilter = caloVsPFMetFilter.clone(
#        CaloMetInputTag  = cms.InputTag('met'),
#        PFMetInputTag    = cms.InputTag('pfMet'),
#        MinCaloOverPFMet = cms.double(0.5),
#        SizeOfDeltaPhiWindowInNPi = cms.double(1.),
#        TaggingMode      = cms.bool(True)
#    )
    
    ## Additional event list for Hcal Laser Filter _______________________________||
    from RecoMET.METFilters.multiEventFilter_cfi import multiEventFilter
    process.HCALLaserEvtFilterList2012 = multiEventFilter.clone(
        file        = cms.FileInPath('Calibration/CalibTreeMaker/data/HCALLaserEventList_20Nov2012-v2_Jet_JetHT_JetMon.txt'),
        taggingMode = cms.bool(False)
        )

    # sequence with filters
    process.filterSequence = cms.Sequence(
        process.hltHighLevel *
        process.stdCleaningSequence *
        process.HCALLaserEvtFilterList2012 
#        process.RA2CaloVsPFMETFilter
        )

    if not isData:
        process.filterSequence.remove( process.hltHighLevel )
        process.filterSequence.remove( process.HCALLaserEvtFilterList2012 )



    # ---- Tree makers ------------------------------------------------------------
    process.load("Calibration.CalibTreeMaker.CalibTreeMaker_cff")

    if isData:
        process.tmAK5JPTL1Offset = process.calibTreeMakerJPTData.clone(
            TreeName                       = treeName,
            WritePhotons                   = writePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5CaloL1Offset = process.calibTreeMakerCaloData.clone(
            TreeName                       = treeName,
            WritePhotons                   = writePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5CaloL1FastJet = process.calibTreeMakerAK5FastCaloData.clone(
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5PFL1FastJet = process.calibTreeMakerAK5FastPFData.clone(
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5PFL1CHS = process.calibTreeMakerAK5PFCHSData.clone(
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")          
            )
    
        process.tmAK5withNuPFL1CHS = process.calibTreeMakerAK5PFCHSData.clone(
            OutputFile                     = cms.string('ak5withNuPFCHS.root'),
            NJet_GenJets                   = cms.InputTag("ak5GenJets"),
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")          
            )
    
        process.products = cms.Sequence(
            process.calibjets *
            process.produceAllCaloMETCorrections *
            process.produceAllPFMETCorrections *
            process.produceAllPFCHSMETCorrections
            )
    if not isData:
        process.tmAK5JPTL1Offset = process.calibTreeMakerJPT.clone(
            TreeName                       = treeName,
            WritePhotons                   = writePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5CaloL1Offset = process.calibTreeMakerCalo.clone(
            TreeName                       = treeName,
            WritePhotons                   = writePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5CaloL1FastJet = process.calibTreeMakerAK5FastCalo.clone(
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5PFL1FastJet = process.calibTreeMakerAK5FastPF.clone(
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")      
            )
    
        process.tmAK5PFL1CHS = process.calibTreeMakerAK5PFCHS.clone(
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")          
            )
    
        process.tmAK5withNuPFL1CHS = process.calibTreeMakerAK5PFCHS.clone(
            OutputFile                     = cms.string('ak5withNuPFCHS.root'),
            NJet_GenJets                   = cms.InputTag("ak5GenJets"),
            TreeName                       = process.tmAK5CaloL1Offset.TreeName,
            WritePhotons                   = process.tmAK5CaloL1Offset.WritePhotons,
            NJet_BoolTags                  = cms.VInputTag("RA2CaloVsPFMETFilter")          
            )

        process.products = cms.Sequence(
            process.calibTreeMakerGenJetsNoNuNoMuNoNu *
#            genJetParticles * recoGenJets * recoAllGenJetsNoNu
            process.calibjets *
            process.produceAllCaloMETCorrections *
            process.produceAllPFMETCorrections *
            process.produceAllPFCHSMETCorrections *
            process.genPhotons *
            process.goodGenPhotons *
            process.myPartons *
#            process.JPTJetPartonMatching *
            process.CaloJetPartonMatching *
            process.PFJetPartonMatching *
            process.AK5PFCHSJetPartonMatching
            )


    # ---- Path -------------------------------------------------------------------
    process.dump = cms.EDAnalyzer("EventContentAnalyzer")
    process.makeTrees = cms.Path(
        process.filterSequence *
#        process.dump *
        process.products *
        process.softElectronCands *
#        process.ak5JPTJetsBtag *
#        process.tmAK5JPTL1Offset *
        process.ak5CaloJetsBtag *
        process.tmAK5CaloL1FastJet *
        process.ak5PFJetsBtag *
        process.tmAK5PFL1FastJet *
        process.ak5PFCHSJetsBtag *
        process.tmAK5PFL1CHS*
        process.tmAK5withNuPFL1CHS
        )

    process.schedule = cms.Schedule(process.makeTrees)




