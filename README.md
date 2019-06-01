# Twitter Scrape

Another kubernetes twitter scraping job

Complete with Kubernetes yaml file to apply.  Download the yaml files and run the job. You'll need to create a Kubernetes Secret with your access tokens first: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: twitter
type: Opaque
data:
  key: baseencode64key
  secret: baseencode64secret
  token: baseencode64token
  token_secret: baseencode64token_secret
```
