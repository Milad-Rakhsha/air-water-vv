from proteus.default_n import *
from proteus import (StepControl,
                     TimeIntegration,
                     NonlinearSolvers,
                     LinearSolvers,
                     LinearAlgebraTools)
from proteus.mprans import VOF
from proteus import Context
import vof_p as physics


ct = Context.get()
runCFL = ct.runCFL
nLevels = ct.nLevels
parallelPartitioningtype = ct.parallelPartitioningType
nLayersOfOverlapForParallel = ct.nLayersOfOverlapForParallel
restrictFineSolutionToAllMeshes = ct.restrictFineSolutionToAllMeshes
triangleOptions = ct.triangleOptions


timeIntegration = TimeIntegration.BackwardEuler_cfl
stepController  = StepControl.Min_dt_controller

femSpaces = {0:ct.basis}
elementQuadrature = ct.elementQuadrature
elementBoundaryQuadrature = ct.elementBoundaryQuadrature

massLumping       = False
numericalFluxType = VOF.NumericalFlux
conservativeFlux  = None
subgridError      = VOF.SubgridError(coefficients=physics.coefficients,
                                     nd=ct.domain.nd)

shockCapturing    = VOF.ShockCapturing(physics.coefficients,
                                       ct.domain.nd,
                                       shockCapturingFactor=ct.vof_shockCapturingFactor,
                                       lag=ct.vof_lag_shockCapturing)

fullNewtonFlag = True
multilevelNonlinearSolver = NonlinearSolvers.Newton
levelNonlinearSolver      = NonlinearSolvers.Newton

nonlinearSmoother = None
linearSmoother    = None

matrix = LinearAlgebraTools.SparseMatrix

if ct.useOldPETSc:
    multilevelLinearSolver = LinearSolvers.PETSc
    levelLinearSolver      = LinearSolvers.PETSc
else:
    multilevelLinearSolver = LinearSolvers.KSP_petsc4py
    levelLinearSolver      = LinearSolvers.KSP_petsc4py

if ct.useSuperlu:
    multilevelLinearSolver = LinearSolvers.LU
    levelLinearSolver      = LinearSolvers.LU

linear_solver_options_prefix = 'vof_'
levelNonlinearSolverConvergenceTest = 'r'
linearSolverConvergenceTest         = 'r-true'

tolFac      = 0.0
nl_atol_res = ct.vof_nl_atol_res

linTolFac   = 0.001
l_atol_res = 0.001*vof_nl_atol_res

useEisenstatWalker = False

maxNonlinearIts = 50
maxLineSearches = 0

auxiliaryVariables = ct.domain.auxiliaryVariables

auxiliaryVariables = [columnGauge]
