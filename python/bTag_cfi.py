import FWCore.ParameterSet.Config as cms

from RecoBTag.Configuration.RecoBTag_cff import *

from RecoJets.JetAssociationProducers.j2tParametersVX_cfi import *
ic5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
    j2tParametersVX,
    jets = cms.InputTag("iterativeCone5PFJets")
)



# create a new jets and tracks association
#ak5Calo
ak5CaloJetTracksAssociatorAtVertex = ic5JetTracksAssociatorAtVertex.clone()
ak5CaloJetTracksAssociatorAtVertex.jets = "ak5CaloJets"
ak5CaloJetTracksAssociatorAtVertex.tracks = "generalTracks"
ak5CaloImpactParameterTagInfos = impactParameterTagInfos.clone()
ak5CaloImpactParameterTagInfos.jetTracks = "ak5CaloJetTracksAssociatorAtVertex"
ak5CaloSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
ak5CaloSecondaryVertexTagInfos.trackIPTagInfos = "ak5CaloImpactParameterTagInfos"
ak5CaloSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
ak5CaloSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("ak5CaloSecondaryVertexTagInfos") )
ak5CaloJetBtaggingSV = cms.Sequence(
                                    ak5CaloImpactParameterTagInfos *
                                    ak5CaloSecondaryVertexTagInfos * 
                                    ak5CaloSimpleSecondaryVertexBJetTags
                                   )
ak5CaloJetsBtag = cms.Sequence(
                               ak5CaloJetTracksAssociatorAtVertex *
                               ak5CaloJetBtaggingSV
                              )

#ak5PF
ak5PFJetTracksAssociatorAtVertex = ic5JetTracksAssociatorAtVertex.clone()
ak5PFJetTracksAssociatorAtVertex.jets = "ak5PFJets"
ak5PFJetTracksAssociatorAtVertex.tracks = "generalTracks"
ak5PFImpactParameterTagInfos = impactParameterTagInfos.clone()
ak5PFImpactParameterTagInfos.jetTracks = "ak5PFJetTracksAssociatorAtVertex"
ak5PFSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
ak5PFSecondaryVertexTagInfos.trackIPTagInfos = "ak5PFImpactParameterTagInfos"
ak5PFSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
ak5PFSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("ak5PFSecondaryVertexTagInfos") )
ak5PFJetBtaggingSV = cms.Sequence(
                                    ak5PFImpactParameterTagInfos *
                                    ak5PFSecondaryVertexTagInfos * 
                                    ak5PFSimpleSecondaryVertexBJetTags
                                   )
ak5PFJetsBtag = cms.Sequence(
                               ak5PFJetTracksAssociatorAtVertex *
                               ak5PFJetBtaggingSV
                              )

#ak5JPT
ak5JPTJetTracksAssociatorAtVertex = ic5JetTracksAssociatorAtVertex.clone()
ak5JPTJetTracksAssociatorAtVertex.jets = "JetPlusTrackZSPCorJetAntiKt5"
ak5JPTJetTracksAssociatorAtVertex.tracks = "generalTracks"
ak5JPTImpactParameterTagInfos = impactParameterTagInfos.clone()
ak5JPTImpactParameterTagInfos.jetTracks = "ak5JPTJetTracksAssociatorAtVertex"
ak5JPTSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
ak5JPTSecondaryVertexTagInfos.trackIPTagInfos = "ak5JPTImpactParameterTagInfos"
ak5JPTSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
ak5JPTSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("ak5JPTSecondaryVertexTagInfos") )
ak5JPTJetBtaggingSV = cms.Sequence(
                                    ak5JPTImpactParameterTagInfos *
                                    ak5JPTSecondaryVertexTagInfos * 
                                    ak5JPTSimpleSecondaryVertexBJetTags
                                   )
ak5JPTJetsBtag = cms.Sequence(
                               ak5JPTJetTracksAssociatorAtVertex *
                               ak5JPTJetBtaggingSV
                              )

#ak7Calo
ak7CaloJetTracksAssociatorAtVertex = ic5JetTracksAssociatorAtVertex.clone()
ak7CaloJetTracksAssociatorAtVertex.jets = "ak7CaloJets"
ak7CaloJetTracksAssociatorAtVertex.tracks = "generalTracks"
ak7CaloImpactParameterTagInfos = impactParameterTagInfos.clone()
ak7CaloImpactParameterTagInfos.jetTracks = "ak7CaloJetTracksAssociatorAtVertex"
ak7CaloSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
ak7CaloSecondaryVertexTagInfos.trackIPTagInfos = "ak7CaloImpactParameterTagInfos"
ak7CaloSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
ak7CaloSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("ak7CaloSecondaryVertexTagInfos") )
ak7CaloJetBtaggingSV = cms.Sequence(
                                    ak7CaloImpactParameterTagInfos *
                                    ak7CaloSecondaryVertexTagInfos * 
                                    ak7CaloSimpleSecondaryVertexBJetTags
                                   )
ak7CaloJetsBtag = cms.Sequence(
                               ak7CaloJetTracksAssociatorAtVertex *
                               ak7CaloJetBtaggingSV
                              )

#ak7PF
ak7PFJetTracksAssociatorAtVertex = ic5JetTracksAssociatorAtVertex.clone()
ak7PFJetTracksAssociatorAtVertex.jets = "ak7PFJets"
ak7PFJetTracksAssociatorAtVertex.tracks = "generalTracks"
ak7PFImpactParameterTagInfos = impactParameterTagInfos.clone()
ak7PFImpactParameterTagInfos.jetTracks = "ak7PFJetTracksAssociatorAtVertex"
ak7PFSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
ak7PFSecondaryVertexTagInfos.trackIPTagInfos = "ak7PFImpactParameterTagInfos"
ak7PFSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
ak7PFSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("ak7PFSecondaryVertexTagInfos") )
ak7PFJetBtaggingSV = cms.Sequence(
                                    ak7PFImpactParameterTagInfos *
                                    ak7PFSecondaryVertexTagInfos * 
                                    ak7PFSimpleSecondaryVertexBJetTags
                                   )
ak7PFJetsBtag = cms.Sequence(
                               ak7PFJetTracksAssociatorAtVertex *
                               ak7PFJetBtaggingSV
                              )

#ak5PFCHS
ak5PFCHSJetTracksAssociatorAtVertex = ic5JetTracksAssociatorAtVertex.clone()
ak5PFCHSJetTracksAssociatorAtVertex.jets = "ak5PFCHSJets"
ak5PFCHSJetTracksAssociatorAtVertex.tracks = "generalTracks"
ak5PFCHSImpactParameterTagInfos = impactParameterTagInfos.clone()
ak5PFCHSImpactParameterTagInfos.jetTracks = "ak5PFCHSJetTracksAssociatorAtVertex"
ak5PFCHSSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
ak5PFCHSSecondaryVertexTagInfos.trackIPTagInfos = "ak5PFCHSImpactParameterTagInfos"
ak5PFCHSSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
ak5PFCHSSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("ak5PFCHSSecondaryVertexTagInfos") )
ak5PFCHSJetBtaggingSV = cms.Sequence(
                                    ak5PFCHSImpactParameterTagInfos *
                                    ak5PFCHSSecondaryVertexTagInfos * 
                                    ak5PFCHSSimpleSecondaryVertexBJetTags
                                   )
ak5PFCHSJetsBtag = cms.Sequence(
                               ak5PFCHSJetTracksAssociatorAtVertex *
                               ak5PFCHSJetBtaggingSV
                              )

#if some other algorithm is to be included at a later date, see leftovers below

# impact parameter b-tag
#newImpactParameterTagInfos = impactParameterTagInfos.clone()
#newImpactParameterTagInfos.jetTracks = "newJetTracksAssociatorAtVertex"
#newTrackCountingHighEffBJetTags = trackCountingHighEffBJetTags.clone()
#newTrackCountingHighEffBJetTags.tagInfos = cms.VInputTag( cms.InputTag("newImpactParameterTagInfos") )
#newTrackCountingHighPurBJetTags = trackCountingHighPurBJetTags.clone()
#newTrackCountingHighPurBJetTags.tagInfos = cms.VInputTag( cms.InputTag("newImpactParameterTagInfos") )
#newJetProbabilityBJetTags = jetProbabilityBJetTags.clone()
#newJetProbabilityBJetTags.tagInfos = cms.VInputTag( cms.InputTag("newImpactParameterTagInfos") )
#newJetBProbabilityBJetTags = jetBProbabilityBJetTags.clone()
#newJetBProbabilityBJetTags.tagInfos = cms.VInputTag( cms.InputTag("newImpactParameterTagInfos") )
# secondary vertex b-tag
#newSecondaryVertexTagInfos = secondaryVertexTagInfos.clone()
#newSecondaryVertexTagInfos.trackIPTagInfos = "newImpactParameterTagInfos"
#newSimpleSecondaryVertexBJetTags = simpleSecondaryVertexBJetTags.clone()
#newSimpleSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("newSecondaryVertexTagInfos") )
#newCombinedSecondaryVertexBJetTags = combinedSecondaryVertexBJetTags.clone()
#newCombinedSecondaryVertexBJetTags.tagInfos = cms.VInputTag( cms.InputTag("newImpactParameterTagInfos"), cms.InputTag("newSecondaryVertexTagInfos") )
#newCombinedSecondaryVertexMVABJetTags = combinedSecondaryVertexMVABJetTags.clone()
#newCombinedSecondaryVertexMVABJetTags.tagInfos = cms.VInputTag( cms.InputTag("newImpactParameterTagInfos"), cms.InputTag("newSecondaryVertexTagInfos") )

# prepare a path running the new modules
#ak5CaloJetTracksAssociator = cms.Sequence(
#    ak5CaloJetTracksAssociatorAtVertex
#)

#newJetBtaggingIP = cms.Sequence(
#    newImpactParameterTagInfos * (
#        newTrackCountingHighEffBJetTags +
#        newTrackCountingHighPurBJetTags +
#        newJetProbabilityBJetTags +
#        newJetBProbabilityBJetTags
#    )
#)

#newJetBtaggingSV = cms.Sequence(
#    newImpactParameterTagInfos *
#    newSecondaryVertexTagInfos * (
#        newSimpleSecondaryVertexBJetTags #+
        #newCombinedSecondaryVertexBJetTags +
        #newCombinedSecondaryVertexMVABJetTags
#    )
#)

#newJetBtagging = cms.Sequence(
#    newJetBtaggingIP +
#    newJetBtaggingSV
#)












