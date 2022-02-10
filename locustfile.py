from locust import HttpUser, task
import random

projects = [

]

TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpXYkhLcUtMeGxIVDdNX2lpbHVLVSJ9.eyJodHRwczovLzRpbnRlbGxpZ2VuY2UuY29tLmJyL2VtYWlsIjoiYWRtaW5ANGNhc3RodWIuY29tLmJyIiwiaHR0cHM6Ly80aW50ZWxsaWdlbmNlLmNvbS5ici91c2VyX21ldGFkYXRhIjp7fSwiaHR0cHM6Ly80aW50ZWxsaWdlbmNlLmNvbS5ici9hcHBfbWV0YWRhdGEiOnsicm9sZXMiOlsiaXM0aSIsImlzT0NCIiwiaXNFZGl0b3IiLCJpc0ZhYVMiLCJpc1NURyJdLCJjb21wYW55IjoiSGVyaW5nIn0sImlzcyI6Imh0dHBzOi8vZGV2ZWxvcG1lbnQtNGludGVsbGlnZW5jZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBlNzQzYTIwNGY0OWEwMDZmZTRkNGQ1IiwiYXVkIjoiNGNhc3RodWIiLCJpYXQiOjE2NDE0MTIwNTYsImV4cCI6MTY0MTQ5ODQ1NiwiYXpwIjoiRGRVTjlWVkFFOXk5ZnhaZVBTdmZKYmdBbWNxZUlpakIiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTpwcm9qZWN0cyIsInJlYWQ6Y3VycmVudF91c2VyIiwicmVhZDpwcm9qZWN0cyJdfQ.wd4TbgGgd2MLQAxaAjHvLNa98g5kXD6c3jqqqayJhncBPp_fJ_RgJSTlVeRmgugzJnnRk1wLiqQwXug3HCEIlx7Jv2_IGtLl2OQ0ps5PHUlGC4G7RRK_mIjbyw95nZM3k5JsgkPLGyykEVJa0bgxZNf18ulpgFpNjyTXr-GcaFTjwqCwXwusCeDnSzff6ki-GW-xCnTCRiKIZpyucqFlqsR2ZGMb8DgtIrBXU24EqonvCgCfJPk1rR8au4Yz1E9Pxd6aYhNJkmGe-5djasOifnV43ygrw9XV0D41QWRfsZpJ76IOaZ7baeuXClF9EZgKvS7yvWfCHdPpE4c9_CbNqQ"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

PROJECTS = {
    0: {"id": "61c46195b81f6ea9a85b6faa", "y": "forecast_1_quantidade_1"},
    1: {"id": "61c4a4a2b81f6ea9a85b6fad", "y": "forecast_1_caminhoes"},
    2: {"id": "61c4a737b81f6ea9a85b6fae", "y": "forecast_1_quantidade_1"},
    3: {"id": "61c46630b81f6ea9a85b6fac", "y": "forecast_1_quantidade_1"},
    4: {"id": "61c46497b81f6ea9a85b6fab", "y": "forecast_1_quantidade_1"},
    5: {"id": "61c33473b81f6ea9a85b6fa2", "y": "forecast_1_demand"},
    6: {"id": "61c3348bb81f6ea9a85b6fa3", "y": "forecast_1_industria"},
}


class ModelExplorer(HttpUser):

    @task
    def model_info(self):
        project = PROJECTS[random.randint(0, 6)]

        url = "/api/v1/projects/{project_id}/{y}/models/accuracy/MAPE".format(
            project_id=project['id'], y=project['y']
        )
        self.client.get(
            url,
            headers=HEADERS)

    # url = "/api/v1/projects/{project_id}/{y}/model-in-production/arima/1".format(
    #     project_id=project['id'], y=project['y']
    # )
    # self.client.post(
    #     url,
    #     headers=HEADERS)

    # @task
    # def upload(self):

    #     url = "/api/v1/upload"

    #     with open('files/dataset_camb_HDV_DLH.xlsx', 'rb') as _fp:
    #         files = {
    #             "file": (_fp.name, _fp, "application/octet-stream"),
    #         }
    #         data = {
    #             "project_name": "New_project",
    #             "icon_url": "icon_url",
    #         }

    #         self.client.post(
    #             url,
    #             files=files,
    #             data=data,
    #             headers=HEADERS)

    # @task
    # def variables(self):
    #     _projects = [
    #         '61d6e9f765646f62e4de2875',
    #         '61d6e9f765646f62e4de2876',
    #         '61d6e9f765646f62e4de2877',
    #         '61d6e9f865646f62e4de287e',
    #         '61d6e9f865646f62e4de287f',
    #         '61d6e9f865646f62e4de2880',
    #         '61d6e9f865646f62e4de2887',
    #         '61d6e9f865646f62e4de2888',
    #         '61d6e9f865646f62e4de2889',
    #         '61d6e9f865646f62e4de2890'
    #     ]

    #     project_id = _projects[random.randint(0, 6)]
    #     url = f"/api/v1/variables/{project_id}"

    #     data = {
    #         "var_y": "y_hdv_dlh",
    #         "date_var": "data_tidy",
    #         "date_format": "YYYY-MM-DD",
    #         "var_x": [
    #             "pmc",
    #             "xagropec",
    #             "camb",
    #             "ici",
    #             "taxa",
    #             "fina",
    #             "d_du",
    #             "diesel",
    #             "v_comb"
    #         ]
    #     }

    #     self.client.post(
    #         url,
    #         json=data,
    #         headers=HEADERS
    #     )
