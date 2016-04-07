# docker

You can view All Models ( Table  ) in Admin View
host://admin   

Document Search Engine with REST API  

How to use API ?  

host://api/users                : GET Details of all users  
host://api/users/{user_name}    : GET Details of perticular user   
host://api/documents            : GET Details of all uploaded Documents  
host://api/documents/{doc_id}   : GET Detail  of perticular document   
host://api/documents/upload     : POST Upload document by passing filling filling following requirements  
  - doc_title  
  - doc_tags  
  - doc_description  
  - doc_path {attach file  } | file field  
  - doc_type  
  - doc_uploaded_by | username is required which must be in User table  
  
