# arp-project
## /signup/:
  post:
  
    {
      "phone_number": "",
      "first_name": "",
      "last_name": "",
      "email": "",
      "user_province": "",
      "user_city": "",
      "user_lat": null,
      "user_long": null,
      "password": ""
    }

## /signin/:
  post:
  
    {
      "phone_number": "",
      "password": ""
  }

## /token/refresh/:
  post:
  
    {
      "refresh": ""
  }

## /expert/signup/:
  post: send with Brearer token
  
    {
      "father_name": "",
      "expert_province": "",
      "expert_city": "",
      "shaba_number": "",
      "gender": ,
      "military_service": ,
      "married_status": ,
      "expert_lat": "",
      "expert_long": "",
      "skills": ""
  }

## /service/new-service/:
  post: send with Brearer token
  
    {
      "title": "",
  }

## /service/new-skill/:
  post: send with Brearer token
  
    {
      "title": "pride fix",
      "caption": "",
      "service": 4
  }

