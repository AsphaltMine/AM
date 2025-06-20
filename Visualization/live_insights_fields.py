TEST_ROOT_TAGS = {
    "MarshallExp": "marshall",
    "ITSExp": "its",
    "RuttingExp": "rutting",
    "StiffnessExp": "stiffness",
    "TSRSTExp": "tsrst",
    "UTSTExp": "utst",
}

TEST_LABELS = {
    "marshall": "Marshall",
    "its": "ITS",
    "rutting": "Rutting",
    "stiffness": "Stiffness",
    "tsrst": "TSRST",
    "utst": "UTST",
}

MIXTURE_NUMERIC_FIELDS = {
    "binder_content": ("Mixture.MixtureRecipe.Composition.Binder.BinderContent", "Binder Content (%)"),
    "rap_content": ("Mixture.MixtureRecipe.Composition.ReclaimedAsphalt", "RAP Content (%)"),
    "max_density": ("Mixture.MixtureRecipe.MixtureMaximumDensity", "Maximum Density (Mg/m³)"),
    "recovered_penetration": ("Mixture.RecoveredMaterials.Binder.Penetration", "Recovered Penetration (0.1mm)"),
    "recovered_softening_point": ("Mixture.RecoveredMaterials.Binder.SofteningPoint", "Recovered Softening Point (°C)"),
    "recovered_elastic_recovery": ("Mixture.RecoveredMaterials.Binder.ElasticRecovery", "Recovered Elastic Recovery (%)"),
}

MIXTURE_CATEGORICAL_FIELDS = {
    "mixing_method": ("Mixture.Mixing.MixingMethod", "Mixing Method"),
}

MIXTURE_TYPE_FIELD = ("Mixture.MixtureIdentifiers.MixtureType", "MixType")

MIXTURE_TOP_N_FIELDS = {
    "target_binder_grade": ("Mixture.MixtureRecipe.Composition.Binder.TargetBinderGrade", "Target Binder Grade"),
}

YEAR_FIELD = ("DataSource.Year", "Records by Year")

SIEVE_SOURCES = {
    "composition": (
        "Mixture/MixtureRecipe/Composition/AggregatesDistribution/Point",
        "Sieve Gradation – Composition (as designed)",
    ),
    "recovered": (
        "Mixture/RecoveredMaterials/Aggregates/GrainSizeDistribution/Point",
        "Sieve Gradation – Recovered Materials",
    ),
}
SIEVE_POINT_SIZE_TAG = "Size"
SIEVE_POINT_VALUE_TAG = "PercentageDistribution"

TEST_RESULT_FIELDS = {
    "marshall": {
        "stability": ("MarshallTestResults.MarshallResults.Stability", "Stability (kN)"),
        "flow": ("MarshallTestResults.MarshallResults.Flow", "Flow (mm)"),
        "marshall_quotient": ("MarshallTestResults.MarshallResults.MarshallQuotient", "Marshall Quotient (kN/mm)"),
        "bulk_density": ("MarshallTestResults.MarshallResults.BulkDensity.Value", "Bulk Density (Mg/m³)"),
        "air_voids": ("MarshallTestResults.MarshallResults.Voids.AirVoids", "Air Voids (%)"),
        "vma": ("MarshallTestResults.MarshallResults.Voids.MineralAggregateVoids", "VMA (%)"),
        "vfb": ("MarshallTestResults.MarshallResults.Voids.VoidsFilledWithBitumen", "VFB (%)"),
    },
    "its": {
        "test_temperature": ("ITSTestResults.ITSResults.TestTemperature", "Test Temperature (°C)"),
        "itsr": ("ITSTestResults.ITSResults.IndirectTensileStrengthRatio", "ITSR (%)"),
        "its_dry": ("ITSTestResults.ITSResults.Dry.Mean.IndirectTensileStrength", "ITS Dry (kPa)"),
        "its_wet": ("ITSTestResults.ITSResults.Wet.Mean.IndirectTensileStrength", "ITS Wet (kPa)"),
    },
    "rutting": {
        "test_temperature": ("RuttingTestResults.Results.TestTemperature", "Test Temperature (°C)"),
        "rut_depth": (
            "RuttingTestResults.Results.Procedure.LargeOrExtraLargeDevices.Mean.MeanProportionalRutDepth",
            "Mean Proportional Rut Depth (%)",
        ),
    },
    "stiffness": {},
    "tsrst": {
        "start_temperature": ("TSRSTestResults.TSRSTResults.StartTemperature", "Start Temperature (°C)"),
        "temperature_rate": ("TSRSTestResults.TSRSTResults.TemperatureRate", "Temperature Rate (°C/h)"),
        "failure_stress": ("TSRSTestResults.TSRSTResults.FailureStress", "Failure Stress (MPa)"),
        "failure_temperature": ("TSRSTestResults.TSRSTResults.FailureTemperature", "Failure Temperature (°C)"),
    },
    "utst": {
        "test_temperature": ("UTSTestResults.UTSTResults.TestTemperature", "Test Temperature (°C)"),
        "deformation_rate": ("UTSTestResults.UTSTResults.AppliedDeformationRate", "Applied Deformation Rate (%/min)"),
        "tensile_strength": ("UTSTestResults.UTSTResults.TensileStrength", "Tensile Strength (MPa)"),
        "failure_strain": ("UTSTestResults.UTSTResults.FailureStrain", "Failure Strain (%)"),
    },
}

STIFFNESS_CASE_PATH = "StiffnessTestResults/Results/Case"
STIFFNESS_MODULUS_TAG = "StiffnessModulus"

RECOVERED_FINES_SIEVE_SIZE = 0.063

CORRELATION_FIELDS = {
    "marshall": {
        "default": ["binder_content", "rap_content", "max_density", "recovered_0063", "stability", "flow", "air_voids"],
        "extra": ["marshall_quotient", "bulk_density", "recovered_penetration", "recovered_softening_point"],
    },
    "its": {
        "default": ["binder_content", "rap_content", "max_density", "recovered_0063", "itsr"],
        "extra": ["test_temperature", "its_dry", "its_wet", "recovered_penetration", "recovered_softening_point"],
    },
    "rutting": {
        "default": ["binder_content", "rap_content", "max_density", "recovered_0063", "rut_depth"],
        "extra": ["test_temperature", "recovered_penetration", "recovered_softening_point"],
    },
    "stiffness": {
        "default": ["binder_content", "rap_content", "max_density", "recovered_0063", "stiffness_modulus"],
        "extra": ["recovered_penetration", "recovered_softening_point"],
    },
    "tsrst": {
        "default": ["binder_content", "rap_content", "max_density", "recovered_0063", "failure_stress", "failure_temperature"],
        "extra": ["start_temperature", "temperature_rate", "recovered_penetration", "recovered_softening_point"],
    },
    "utst": {
        "default": ["binder_content", "rap_content", "max_density", "recovered_0063", "tensile_strength", "failure_strain"],
        "extra": ["test_temperature", "deformation_rate", "recovered_penetration", "recovered_softening_point"],
    },
}

MIN_CORRELATION_N = 10
