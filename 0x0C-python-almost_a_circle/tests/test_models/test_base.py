def test_base_tojsonstringnone(self):
    ret = "[]"
    test_list = self.base_1.to_json_string(None)
    self.assertEqual(ret, test_list)

def test_base_tojsonstringempty(self):
    ret = "[]"
    test_list = self.base_1.to_json_string([])
    self.assertEqual(ret, test_list)

def test_base_tojsonstringdict(self):
    test_dict = [{'id': 7}]
    ret = "[{"id": 7}]"
    self.assertEqual(self.base_1.to_json_string(test_dict), ret)

def test_base_fromjsonstringnone(self):
    ret = []
    test_list = self.base_1.from_json_string(None)
    self.assertEqual(ret, test_list)

def test_base_fromjsonstringempty(self):
    ret = []
    test_list = self.base_1.from_json_string([])
    self.assertEqual(ret, test_list)

def test_base_fromjsonstringdict(self):
    ret = [{'id': 7}]
    test_dict = "[{"id": 7}]"
    self.assertEqual(self.base_1.from_json_string(test_dict), ret)
