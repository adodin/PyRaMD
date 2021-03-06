import numpy as np

from .context import PyRaMD


def test_velocity_verlet_0v():
    x = np.ones((3, 10))
    v = np.zeros((3, 10))
    m = np.ones((1, 10))
    id_gas = PyRaMD.force.IdealGas()
    v_verlet = PyRaMD.integrate.VelocityVerlet(0.1, id_gas)
    x, v = v_verlet(x,v,m)
    assert np.sum(x == np.ones((3, 10))) == 30
    assert np.sum(v == np.zeros((3, 10))) == 30
    assert np.sum(m == np.ones((1, 10))) == 10


def test_velocity_verlet():
    x = np.ones((3, 10))
    v = np.ones((3, 10))
    m = np.ones((1, 10))
    id_gas = PyRaMD.force.IdealGas()
    v_verlet = PyRaMD.integrate.VelocityVerlet(0.1, id_gas)
    x, v = v_verlet(x, v, m)
    assert np.sum(x == np.ones((3, 10)) + 0.1 * np.ones((3, 10))) == 30
    assert np.sum(v == np.ones((3, 10))) == 30
    assert np.sum(m == np.ones((1, 10))) == 10