from Para_Proc.Param import cube_avg

def test_2x2x2_cube():
    arr = np.arange(8).reshape((2,2,2))
    expected = np.array([
        arr[0,0,0], arr[0,0,1], arr[0,1,0], arr[0,1,1],
        arr[1,0,0], arr[1,0,1], arr[1,1,0], arr[1,1,1]
    ])
    assert np.array_equal(cube_avg(arr), expected)

def test_4x4x4_cube():
    arr = np.ones((4,4,4))*5
    assert np.allclose(cube_avg(arr), np.ones(8)*5)