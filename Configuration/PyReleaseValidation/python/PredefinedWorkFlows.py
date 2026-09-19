#! /usr/bin/env python3

class PredefinedWorkFlows(dict):
    """
    Dict of predefined workflow sets. The keys are defined upfront,
    and the values are lazily filled via load() on first access
    because the import of relval_Run4.prefixDet is slow.
    """

    _KEYS = (
        'run1_run2',
        'run3',
        'phase2',
        'heavyIons',
        'jetmc',
        'metmc',
        'muonmc',
        'ph2_hlt',
        'limited',
    )

    def __init__(self):
        super().__init__()
        self._loaded = False
        for key in self._KEYS:
            dict.__setitem__(self, key, None)

    def load(self):
        """Fill in the real values. Safe to call more than once."""
        if self._loaded:
            return
        print(">> Loading predefined workflow sets...")
        from Configuration.PyReleaseValidation.relval_Run4 import prefixDet # slow

        # See README for further details
        # https://github.com/cms-sw/cmssw/tree/master/Configuration/PyReleaseValidation
        self['run1_run2'] = [
            ###### MC (generated from scratch or from RelVal)
            # Run1
            5.1,        # TTbar_8TeV_TuneCUETP8M1       FastSim
            8,          # RelValBeamHalo                Cosmics
            9.0,        # RelValHiggs200ChargedTaus
            25,         # RelValTTbar
            101.0,      # SingleElectronE120EHCAL       + ECALHCAL.customise + fullMixCustomize_cff.setCrossingFrameOn

            # Run2
            7.3,        # UndergroundCosmicSPLooseMu
            1306.0,     # RelValSingleMuPt1_UP15
            1330,       # RelValZMM_13
            135.4,      # ZEE_13TeV_TuneCUETP8M1

            ###### pp Data
            ## Run1
            4.22,       # Run2011A  Cosmics
            4.53,       # Run2012B  Photon                      miniAODs
            1000,       # Run2011A  MinimumBias Prompt          RecoTLR.customisePrompt
            1001,       # Run2011A  MinimumBias                 Data+Express
            ## Run2
            136.731,    # Run2016B SinglePhoton
            136.793,    # Run2017C DoubleEG
            136.874,    # Run2018C EGamma
        ]

        self['run3'] = [
            ###### MC (generated from scratch or from RelVals)
            # Run3
            11634.0,    # TTbar_14TeV                   2021
            13234.0,    # RelValTTbar_14TeV             2021 FastsSim
            12434.0,    # RelValTTbar_14TeV             2023
            12834.0,    # RelValTTbar_14TeV             2024
            12846.0,    # RelValZEE_13                  2024
            16834.0,    # RelValTTbar_14TeV             2025
            17034.96,   # RelValTTbar_14TeV             2025 Hybrid PU
            14034.0,    # RelValTTbar_14TeV             Run3_2023_FastSim
            18434.0,    # RelValTTbar_14TeV             2026

            ###### pp Data
            ## Run3
            # 2021
            139.001,    # Run2021  MinimumBias                  Commissioning2021

            # 2022
            2022.0010001,     # Run2022C JetHT

            # 2023
            2023.0020001,     # Run2023D JetMET0

            # 2024
            2024.0000001,      # Run2024B ZeroBias
            2024.0010001,      # Run2024C JetMET0
            2024.0020001,      # Run2024D EGamma0
            2024.0030001,      # Run2024E DisplacedJet
            2024.0040001,      # Run2024F ParkingDoubleMuonLowMass0
            2024.0050001,      # Run2024G BTagMu
            2024.0060001,      # Run2024H Muon0
            2024.0070001,      # Run2024I Tau

            # 2025
            2025.0000002,     # Run2025B ZeroBias                       noPAT
            2025.0010001,     # Run2025C JetMET0
        ]

        self['heavyIons'] = [
            ###### Heavy Ions
            ## Data
            # Run2
            140.56,    # HIRun2018A HIHardProbes                    Run2_2018_pp_on_AA
            ## MC
        ]

        self['jetmc'] = [5.1, 13, 15, 25, 38, 39]  # MC
        self['metmc'] = [5.1, 15, 25, 37, 38, 39]  # MC
        self['muonmc'] = [5.1, 124.4, 124.5, 20, 21, 22, 23, 25, 30]  # MC

        self['phase2'] = [
            ###### MC (generated from scratch or from RelVals)
            # Phase2
            prefixDet+34.0,	    # RelValTTbar_14TeV                     phase2_realistic_T35        ExtendedRun4D127         (Phase-2 baseline)
            prefixDet+234.0,	# RelValTTbar_14TeV                     phase2_realistic_T35        ExtendedRun4D127         AVE_200_BX_25ns	(Phase-2 baseline with PU)
            prefixDet+34.911,	# TTbar_14TeV_TuneCP5                   phase2_realistic_T35        DD4hepExtendedRun4D127   DD4Hep (HLLHC14TeV BeamSpot)
            #prefixDet+234.999, # RelValTTbar_14TeV (PREMIX)            phase2_realistic_T35        ExtendedRun4D127         AVE_50_BX_25ns_m3p3 COMMENT: reads old format file
            prefixDet+96.0,     # RelValCloseByPGun_CE_E_Front_120um    phase2_realistic_T35        ExtendedRun4D127
            prefixDet+100.0,    # RelValCloseByPGun_CE_H_Coarse_Scint   phase2_realistic_T35        ExtendedRun4D127
            #23234.0,           # Need new workflow with HFNose
            prefixDet+34.75,    # RelValTTbar_14TeV                     phase2_realistic_T35        ExtendedRun4D127         (Phase-2 baseline -  but using timing menu, and only up to step 2)
        ]

        self['ph2_hlt'] = [
            prefixDet+34.75,    # HLT phase-2 timing menu
            prefixDet+34.7501,  # HLT phase-2 tracking-only menu
            prefixDet+34.7502,  # HLT phase-2 tracking menu with tracking ntuple
            prefixDet+34.7503,  # HLT phase-2 menu, CPU vs. GPU validation
            prefixDet+34.751,   # HLT phase-2 timing menu Alpaka variant
            prefixDet+34.7521,  # HLT phase-2 timing menu ticlv5TrackLinkGNN variant
            prefixDet+34.7522,  # HLT phase-2 timing menu mtd_at_hlt variant
            prefixDet+34.753,   # HLT phase-2 timing menu legacy tracking
            prefixDet+34.754,   # HLT phase-2 timing menu legacy tracking with Patatrack quads
            prefixDet+34.755,   # HLT phase-2 timing menu LST building variant
            prefixDet+34.756,   # HLT phase-2 timing menu trimmed tracking
            prefixDet+34.757,   # HLT phase-2 timing menu mkFit fitting variant
            prefixDet+34.758,   # HLT phase-2 timing menu ticl_barrel variant
            prefixDet+34.759,   # HLT phase-2 menu, with NANO:@Phase2HLT
            prefixDet+34.7591,  # HLT phase-2 menu, with NANO:@Phase2HLTVal
            prefixDet+34.7592,  # HLT phase-2 menu, with NANO:@Phase2HLT + DQM
            prefixDet+34.77,    # HLT phase-2 NGT Scouting menu
            prefixDet+34.771,   # HLT phase-2 NGT Scouting menu, Alpaka, TICL-Barrel
            prefixDet+34.772,   # HLT phase-2 NGT Scouting menu, with NANO:@NGTScouting
            prefixDet+34.7721,  # HLT phase-2 NGT Scouting menu, with NANO:@NGTScouting + DQM
            prefixDet+34.773,   # HLT phase-2 NGT Scouting menu, with NANO:@NGTScoutingVal
            prefixDet+34.774,   # HLT phase-2 NGT Scouting menu, with NANO:@NGTScoutingVal+@Phase2L1DPGwithGen
            prefixDet+34.775    # HLT phase-2 NGT Scouting menu, Phase2CAExtension&LSTT5 as GeneralTracks
        ]

        self._loaded = True # set here to avoid recursion via __getitem__ by the next lines
        self['limited'] = (
            self['run1_run2'] +
            self['run3'] +
            self['phase2'] +
            self['heavyIons']
        )

        # check hardcoded dictionaries are complete
        invalid = { k: v for k, v in self.items() if not v }
        assert set(self.keys()) == set(_KEYS), f"load() must set exactly the keys declared in _KEYS={_KEYS}; got {self.keys()}"
        assert not invalid, f"found predefined workflow sets that were not properly initialized: {invalid}"

    def __getitem__(self, key):
        if not self._loaded:
            self.load()
        return dict.__getitem__(self, key)

    def items(self):
        if not self._loaded:
            self.load()
        return dict.items(self)
