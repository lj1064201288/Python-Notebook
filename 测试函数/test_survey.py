import unittest

from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spaish', 'Mandarin']


    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        #my_survey.store_response('English')

        #self.assertIn('English', my_survey.responses)

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_single_responses(self):
        """测试三个答案被妥善的处理"""
        #question = "What language did you first learn to speak?"
        #my_survey = AnonymousSurvey(question)
        #responses = ['English', 'Spanish', 'Mandarin']
        for response in self.responses:
            #my_survey.store_response(response)
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


unittest.main()

