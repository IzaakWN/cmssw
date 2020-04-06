import FWCore.ParameterSet.Config as cms

trackingMaterialAnalyser = cms.EDAnalyzer("TrackingMaterialAnalyser",
    MaterialAccounting      = cms.InputTag("trackingMaterialProducer"),
    SplitMode               = cms.string("NearestLayer"),
    SkipBeforeFirstDetector = cms.bool(False),
    SkipAfterLastDetector   = cms.bool(True),
    SaveSummaryPlot         = cms.bool(True),
    SaveDetailedPlots       = cms.bool(False),
    SaveParameters          = cms.bool(True),
    SaveXML                 = cms.bool(True),
    isHGCal                 = cms.bool(False),
    isHFNose                = cms.bool(False),
    Groups = cms.vstring(
"TrackerRecMaterialPixelBarrelLayer0_External",
"TrackerRecMaterialPixelBarrelLayer1_External",
"TrackerRecMaterialPixelBarrelLayer2_External",
"TrackerRecMaterialPixelBarrelLayer3_External",
"TrackerRecMaterialPixelBarrelLayer0",
"TrackerRecMaterialPixelBarrelLayer1",
"TrackerRecMaterialPixelBarrelLayer2",
"TrackerRecMaterialPixelBarrelLayer3",
"TrackerRecMaterialTIBLayer0_Z0",
"TrackerRecMaterialTIBLayer0_Z20",
"TrackerRecMaterialTIBLayer1_Z0",
"TrackerRecMaterialTIBLayer1_Z30",
"TrackerRecMaterialTIBLayer2_Z0",
"TrackerRecMaterialTIBLayer2_Z40",
"TrackerRecMaterialTIBLayer3_Z0",
"TrackerRecMaterialTIBLayer3_Z50",
"TrackerRecMaterialTOBLayer0_Z0",
"TrackerRecMaterialTOBLayer0_Z20",
"TrackerRecMaterialTOBLayer0_Z70",
"TrackerRecMaterialTOBLayer1_Z0",
"TrackerRecMaterialTOBLayer1_Z20",
"TrackerRecMaterialTOBLayer1_Z80",
"TrackerRecMaterialTOBLayer2_Z0",
"TrackerRecMaterialTOBLayer2_Z25",
"TrackerRecMaterialTOBLayer2_Z80",
"TrackerRecMaterialTOBLayer3_Z0",
"TrackerRecMaterialTOBLayer3_Z25",
"TrackerRecMaterialTOBLayer3_Z80",
"TrackerRecMaterialTOBLayer4_Z0",
"TrackerRecMaterialTOBLayer4_Z25",
"TrackerRecMaterialTOBLayer4_Z80",
"TrackerRecMaterialTOBLayer5_Z0",
"TrackerRecMaterialTOBLayer5_Z25",
"TrackerRecMaterialTOBLayer5_Z80",
"TrackerRecMaterialPixelEndcapDisk1Fw_Inner",
"TrackerRecMaterialPixelEndcapDisk1Fw_Outer",
"TrackerRecMaterialPixelEndcapDisk2Fw_Inner",
"TrackerRecMaterialPixelEndcapDisk2Fw_Outer",
"TrackerRecMaterialPixelEndcapDisk3Fw_Inner",
"TrackerRecMaterialPixelEndcapDisk3Fw_Outer",
"TrackerRecMaterialPixelEndcapDisk1Bw_Inner",
"TrackerRecMaterialPixelEndcapDisk1Bw_Outer",
"TrackerRecMaterialPixelEndcapDisk2Bw_Inner",
"TrackerRecMaterialPixelEndcapDisk2Bw_Outer",
"TrackerRecMaterialPixelEndcapDisk3Bw_Inner",
"TrackerRecMaterialPixelEndcapDisk3Bw_Outer",
"TrackerRecMaterialTIDDisk1_R0",
"TrackerRecMaterialTIDDisk1_R30",
"TrackerRecMaterialTIDDisk2_R25",
"TrackerRecMaterialTIDDisk2_R30",
"TrackerRecMaterialTIDDisk2_R40",
"TrackerRecMaterialTIDDisk3_R24",
"TrackerRecMaterialTECDisk0_R20",
"TrackerRecMaterialTECDisk0_R40",
"TrackerRecMaterialTECDisk0_R50",
"TrackerRecMaterialTECDisk0_R60",
"TrackerRecMaterialTECDisk0_R90",
"TrackerRecMaterialTECDisk1_R20",
"TrackerRecMaterialTECDisk2_R20",
"TrackerRecMaterialTECDisk3",
"TrackerRecMaterialTECDisk4_R33",
"TrackerRecMaterialTECDisk5_R33",
"TrackerRecMaterialTECDisk6",
"TrackerRecMaterialTECDisk7_R40",
"TrackerRecMaterialTECDisk8",
    )
)
