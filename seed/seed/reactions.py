#!/usr/bin/env python
# encoding: utf-8

name = "seed"
shortDesc = ""
longDesc = """

"""
autoGenerated=True
entry(
    index = 0,
    label = "X + X + O2 <=> OX + OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1, n=0, Ea=(28947,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 1,
    label = "X + NH3 <=> NH3X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 2,
    label = "OX + NH3X <=> OHX + NH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.93e+21,'cm^2/(mol*s)'), n=0, Ea=(39560.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 3,
    label = "OX + NH2X <=> OHX + NHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.05e+21,'cm^2/(mol*s)'), n=0, Ea=(104209,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 4,
    label = "OX + NHX <=> NX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.9e+21,'cm^2/(mol*s)'), n=0, Ea=(23157.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 5,
    label = "OHX + NH3X <=> H2OX + NH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.82e+22,'cm^2/(mol*s)'), n=0, Ea=(70437.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 6,
    label = "OHX + NH2X <=> NHX + H2OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.58e+21,'cm^2/(mol*s)'), n=0, Ea=(73332.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 7,
    label = "OHX + NHX <=> NX + H2OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.19e+21,'cm^2/(mol*s)'), n=0, Ea=(41490.7,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 8,
    label = "OHX + OHX <=> OX + H2OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.15e+21,'cm^2/(mol*s)'), n=0, Ea=(71402.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 9,
    label = "X + H2O <=> H2OX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1, n=0, Ea=(0,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 10,
    label = "NX + NX <=> X + X + N2",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.42e+21,'cm^2/(mol*s)'), n=0, Ea=(119648,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 11,
    label = "OX + NX <=> X + NOX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.09e+21,'cm^2/(mol*s)'), n=0, Ea=(82981.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 12,
    label = "NOX <=> X + NO",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.55e+14,'1/s'), n=0, Ea=(225787,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 13,
    label = "NX + NOX <=> X + N2OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.6e+21,'cm^2/(mol*s)'), n=0, Ea=(191050,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 14,
    label = "N2OX <=> X + N2O",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.69e+13,'1/s'), n=0, Ea=(36666.2,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 15,
    label = "X + NH3X <=> H_X + NH2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.52e+20,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 16,
    label = "X + NH2X <=> H_X + NHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.19e+21,'cm^2/(mol*s)'), n=0, Ea=(152454,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 17,
    label = "X + NHX <=> NX + H_X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.35e+21,'cm^2/(mol*s)'), n=0, Ea=(118683,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 18,
    label = "OX + H_X <=> X + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.18e+21,'cm^2/(mol*s)'), n=0, Ea=(123507,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 19,
    label = "H_X + OHX <=> X + H2OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.88e+21,'cm^2/(mol*s)'), n=0, Ea=(91665.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Schneider_Pd211
""",
)

entry(
    index = 20,
    label = "X + NO2 <=> NO2X",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.9, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Nitrogen
""",
)

entry(
    index = 21,
    label = "NO2X <=> OX + NO",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.3e+14,'1/s'), n=0, Ea=(115.5,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Nitrogen
""",
)

entry(
    index = 22,
    label = "OX + NOX <=> X + NO2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.3e+17,'cm^2/(mol*s)'), n=0, Ea=(133,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Nitrogen
""",
)

entry(
    index = 23,
    label = "NOX + H_X <=> NX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.2e+21,'cm^2/(mol*s)'), n=0, Ea=(25,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Nitrogen
""",
)

entry(
    index = 24,
    label = "NO2X + H_X <=> NOX + OHX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.9e+21,'cm^2/(mol*s)'), n=0, Ea=(20,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    longDesc = 
"""
Originally from reaction library: Surface/Nitrogen
""",
)

entry(
    index = 25,
    label = "X + X + H2O <=> H_X + OHX",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.016, n=0, Ea=(51.1949,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [H2O;VacantSite1;VacantSite2]
    Euclidian distance = 3.0
    family: Surface_Adsorption_Dissociative
    Ea raised from 0.0 to 51.2 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [H2O;VacantSite1;VacantSite2]
Euclidian distance = 3.0
family: Surface_Adsorption_Dissociative
Ea raised from 0.0 to 51.2 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 26,
    label = "X + X + NH3 <=> H_X + NH2X",
    degeneracy = 1.5,
    kinetics = StickingCoefficient(A=0.024, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [N;VacantSite1;VacantSite2]
    Euclidian distance = 1.0
    Multiplied by reaction path degeneracy 1.5
    family: Surface_Adsorption_Dissociative"""),
    longDesc = 
"""
Estimated using template [Adsorbate;VacantSite1;VacantSite2] for rate rule [N;VacantSite1;VacantSite2]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 1.5
family: Surface_Adsorption_Dissociative
""",
)

entry(
    index = 27,
    label = "OX + N2OX <=> NX + NO2X",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(3.298e+17,'m^2/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(298,'K'), Tmax=(2000,'K'), comment="""Estimated using template [O;Donating] for rate rule [O;*N-N]
    Euclidian distance = 2.0
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [O;Donating] for rate rule [O;*N-N]
Euclidian distance = 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 28,
    label = "NX + NH3X <=> NHX + NH2X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.94901e+15,'m^2/(mol*s)'), n=0.652756, Ea=(120.135,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*#N]
    Euclidian distance = 2.23606797749979
    Multiplied by reaction path degeneracy 3.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*#N]
Euclidian distance = 2.23606797749979
Multiplied by reaction path degeneracy 3.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 29,
    label = "NX + NH2X <=> NHX + NHX",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.35926e+17,'m^2/(mol*s)'), n=-0.0183333, Ea=(30.05,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Abstracting;*R-H] for rate rule [:N#*;*-N-H]
    Euclidian distance = 3.605551275463989
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;*R-H] for rate rule [:N#*;*-N-H]
Euclidian distance = 3.605551275463989
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 30,
    label = "NHX + NH3X <=> NH2X + NH2X",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(4.94901e+15,'m^2/(mol*s)'), n=0.652756, Ea=(120.135,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*=NH]
    Euclidian distance = 3.1622776601683795
    Multiplied by reaction path degeneracy 3.0
    family: Surface_Abstraction_vdW"""),
    longDesc = 
"""
Estimated using template [AdsorbateVdW;Adsorbate1] for rate rule [N-R;*=NH]
Euclidian distance = 3.1622776601683795
Multiplied by reaction path degeneracy 3.0
family: Surface_Abstraction_vdW
""",
)

entry(
    index = 31,
    label = "X + NOX <=> [Pt]ON=[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.27e+15,'m^2/(mol*s)'), n=0.549, Ea=(7.95274,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Combined;VacantSite]
    Euclidian distance = 0
    family: Surface_DoubleBond_to_Bidentate"""),
    longDesc = 
"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
family: Surface_DoubleBond_to_Bidentate
""",
)

entry(
    index = 32,
    label = "[Pt]ON=[Pt] <=> OX + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.96e+10,'1/s'), n=0.422, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Combined]
    Euclidian distance = 0
    family: Surface_Bidentate_Dissociation"""),
    longDesc = 
"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 33,
    label = "X + X + N2 <=> [Pt]N=N[Pt]",
    degeneracy = 2.0,
    kinetics = StickingCoefficient(A=0.2, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
    Euclidian distance = 0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Adsorption_Bidentate"""),
    longDesc = 
"""
Exact match found for rate rule [Adsorbate;VacantSite1;VacantSite2]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_Adsorption_Bidentate
""",
)

entry(
    index = 34,
    label = "[Pt]N=N[Pt] <=> NX + NX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.96e+10,'1/s'), n=0.422, Ea=(164.329,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Combined]
    Euclidian distance = 0
    family: Surface_Bidentate_Dissociation
    Ea raised from 0.0 to 164.3 kJ/mol to match endothermicity of reaction."""),
    longDesc = 
"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
Ea raised from 0.0 to 164.3 kJ/mol to match endothermicity of reaction.
""",
)

entry(
    index = 35,
    label = "NX + [Pt]ON=[Pt] <=> OX + [Pt]N=N[Pt]",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(4.17963e+17,'m^2/(mol*s)'), n=-0.0183333, Ea=(30.05,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Abstracting;Donating] for rate rule [:N#*;*-O-N]
    Euclidian distance = 3.605551275463989
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;Donating] for rate rule [:N#*;*-O-N]
Euclidian distance = 3.605551275463989
family: Surface_Abstraction
""",
)

entry(
    index = 36,
    label = "X + N2 <=> N#N.[Pt]",
    degeneracy = 1.0,
    kinetics = StickingCoefficient(A=0.1, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""From training reaction 5 used for Adsorbate;VacantSite
    Exact match found for rate rule [Adsorbate;VacantSite]
    Euclidian distance = 0
    family: Surface_Adsorption_vdW"""),
    longDesc = 
"""
From training reaction 5 used for Adsorbate;VacantSite
Exact match found for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_vdW
""",
)

entry(
    index = 37,
    label = "X + N#N.[Pt] <=> [Pt]N=N[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2e+15,'m^2/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Combined;VacantSite]
    Euclidian distance = 0
    Multiplied by reaction path degeneracy 2.0
    family: Surface_vdW_to_Bidentate"""),
    longDesc = 
"""
Exact match found for rate rule [Combined;VacantSite]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Surface_vdW_to_Bidentate
""",
)

entry(
    index = 38,
    label = "[Pt]OO[Pt] <=> OX + OX",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(8.96e+10,'1/s'), n=0.422, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Exact match found for rate rule [Combined]
    Euclidian distance = 0
    family: Surface_Bidentate_Dissociation"""),
    longDesc = 
"""
Exact match found for rate rule [Combined]
Euclidian distance = 0
family: Surface_Bidentate_Dissociation
""",
)

entry(
    index = 39,
    label = "[Pt]OO[Pt] + NX <=> OX + [Pt]ON=[Pt]",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(8.35926e+17,'m^2/(mol*s)'), n=-0.0183333, Ea=(30.05,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Abstracting;Donating] for rate rule [:N#*;*R-O]
    Euclidian distance = 3.1622776601683795
    Multiplied by reaction path degeneracy 2.0
    family: Surface_Abstraction"""),
    longDesc = 
"""
Estimated using template [Abstracting;Donating] for rate rule [:N#*;*R-O]
Euclidian distance = 3.1622776601683795
Multiplied by reaction path degeneracy 2.0
family: Surface_Abstraction
""",
)

entry(
    index = 40,
    label = "X + OH(D) <=> OHX",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = StickingCoefficient(A=0.85, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using an average for rate rule [Adsorbate;VacantSite]
    Euclidian distance = 0
    family: Surface_Adsorption_Single"""),
    longDesc = 
"""
Estimated using an average for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

entry(
    index = 41,
    label = "X + OH(D) <=> OHX",
    degeneracy = 1.0,
    duplicate = True,
    kinetics = StickingCoefficient(A=0.85, n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K'), comment="""Estimated using an average for rate rule [Adsorbate;VacantSite]
    Euclidian distance = 0
    family: Surface_Adsorption_Single"""),
    longDesc = 
"""
Estimated using an average for rate rule [Adsorbate;VacantSite]
Euclidian distance = 0
family: Surface_Adsorption_Single
""",
)

