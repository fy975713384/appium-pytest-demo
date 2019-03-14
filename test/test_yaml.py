from util.operate_yaml import OperateYAML


def test_get_data():
    _yml = OperateYAML(yaml_path='test.yml')
    try:
        res1 = _yml.get_data('a', 'aa')
    except RuntimeError as re:
        assert re.args[0] == '元素格式错误'

    res2 = _yml.get_data('a', 'bb')
    assert res2 == ('id', 'bbb')
