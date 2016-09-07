from proteus.default_p import *
from proteus.mprans import MCorr
from proteus import Context

ct = Context.get()
domain = ct.domain
nd = ct.domain.nd
mesh = domain.MeshOptions


genMesh = mesh.genMesh
movingDomain = ct.movingDomain
T = ct.T

LevelModelType = MCorr.LevelModel

coefficients = MCorr.Coefficients(LSModel_index=ct.LS_model,
                                  V_model=ct.V_model,
                                  me_model=ct.LSC_model,
                                  VOFModel_index=ct.VF_model,
                                  applyCorrection=ct.applyCorrection,
                                  nd=nd,
                                  checkMass=True,
                                  useMetrics=ct.useMetrics,
                                  epsFactHeaviside=ct.epsFact_consrv_heaviside,
                                  epsFactDirac=ct.epsFact_consrv_dirac,
                                  epsFactDiffusion=ct.epsFact_consrv_diffusion)

class zero_phi:
    def __init__(self):
        pass
    def uOfX(self, X):
        return 0.0
    def uOfXT(self, X, t):
        return 0.0

initialConditions = {0: zero_phi()}
