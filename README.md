work in progress: 

```local-auto-deployment-infra ```  
```local-monitoring ```    

```cloud-auto-deployment-infra ```  
```cloud-monitoring ```  

```local and cloud circle-ci pipelines ```  


________________________________________________________________________
 
This repository contains a set of templates and configuration files for webapplication deployment using teraform and ansible.

________________________________________________________________________  
# Requirements:  
``` terraform installed ```  
``` ansible installed ```  
________________________________________________________________________  

# Usage:  

*to init all terraform configuration*      
```$ main.py --init-all``` 

*deploy only network on aws*    
```$ main.py --deploy-network```

*deploy only security on aws (requires network to be deployed)*    
```$ main.py --deploy-secgrp```

*deploy appserver on aws*   
```$ main.py --deploy-appserver```   

*destroy all resources on aws*     
```$ main.py --destroy-all```  

*execute pipeline script on aws server*      
```$ main.py --ssh-exec```      
  
*automatic login using extracted public ip (terraform/ansible/hosts)*  
```./main.py --login```  

*for the help*  
```$ main.py --help```
