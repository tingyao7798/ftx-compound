# ftx-auto-compound

SAM app to auto compound my USD balance in FTX margin lending.

## Setup
* Store FTX API secrets in AWS Secrets Manager
* Create S3 bucket to store SAM package
* Add your secret name and subaccount name(if applicable) template.yaml
  ```yaml
    Environment:
    Variables:
        SECRET_NAME: prod/ftx/api
        SUBACC_NAME: subaccount1
  ```
* Determine a suitable frequency based on APR by https://www.aprtoapy.com/ and customize lambda trigger frequency
  template.yaml
  ```yaml
  Properties:
    Schedule: cron(10 */12 * * ? *)
    Description: compound twice a day at min 10
    Enabled: True
  ```

## Build, Invoke locally and Deploy

Build
```bash
make build
```

Test locally
```
make test
```

Deploy to AWS
```bash
make deploy
```

Cleanup
```
make cleanup
```
