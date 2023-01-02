from rest_framework.test import APITestCase
from . import request_samples, response_samples
from rest_framework import status


class TestEquityEvaluationAPI(APITestCase):
    def setUp(self):
        self.__set_api_urls__()
    
    def __set_api_urls__(self):
        self.vestedEquityValuationURL = '/api/vested_equity_valuation/'

    def __send_stock_evaluation_request__(self, request_data, response_data):
        resp = self.client.post(self.vestedEquityValuationURL, data=request_data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        for index, result in enumerate(resp.data["results"]):
            self.assertDictEqual(result, response_data[index])

    def test_4_years_vesting_with_cliff(self):
        request_data = request_samples.Plan4YearsWithCliffRequest
        response_data = response_samples.Plan4YearsWithCliffResponse
        self.__send_stock_evaluation_request__(request_data, response_data)

    def test_4_years_vesting_without_cliff(self):
        request_data = request_samples.Plan4YearsWithoutCliffRequest
        response_data = response_samples.Plan4YearsWithoutCliffResponse
        self.__send_stock_evaluation_request__(request_data, response_data)

    def test_2_years_with_cliff_and_multiple_evaluations(self):
        request_data = request_samples.Plan2YearsWithCliffAndMultipleEvaluationsRequest
        response_data = response_samples.Plan2YearsWithCliffAndMultipleEvaluationsResponse
        self.__send_stock_evaluation_request__(request_data, response_data)