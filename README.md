# omilia-amazon-connect-integration  
## Integration of Omilia Cloud Platform and Amazon Connect
This repository keeps the AWS Cloudformation template, support scripts and Sample Amazon Connect Flows that will get an Amazon Connect Instance integrate directly with OCP miniApps in a matter of minutes.
The guide and templates assume the user has an Amazon account and an Amazon Connect instance already set up. 

For more information and a step by step guide please download the [Integration Guide](https://omilia.com/wp-content/uploads/2022/04/amazon-connect-integration-step-by-step.pdf).

## AWS CloudFormation template
To run the AWS CloudFormation template using the AWS CLI, you can use the parameters json included in the Templates folder as a template. Change your parameter values as desired. You can see an example usage below: 

```console
aws cloudformation create-stack \
  --stack-name omiliastack \
  --template-body file:///path_to_your_repoitory/Templates/omilia_amazon_connect.yaml  \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters  file:///path_to_your_repository/Templates/parameters.json
```
## Support scripts 

To add your OCP acquired numbers to your integration with Amazon Connect, there's a simple python CLI script that helps doing just that. Provide as parameters, the URL created by your API Gateway, the API Key you created and the numbers, space separated as per the example below: 

```console
python add_numbers.py -u https://wbuj4w6w5f.execute-api.us-east-1.amazonaws.com/prod -k your_api_key_goes_here --numbers +13304708019 +17276084253 +18133950034 +18172038783 +19546211639
```