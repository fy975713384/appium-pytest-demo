from util.operate_yaml import OperateYAML


def test_get_data():
    _yml = OperateYAML(yaml_path='test.yml')
    try:
        _yml.get_data('a', 'aa')
    except RuntimeError as re:
        assert re.args[0] == '元素格式错误'

    res = _yml.get_data('a', 'bb')
    assert res == ('id', 'bbb')
