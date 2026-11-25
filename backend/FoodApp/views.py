from rest_framework.decorators import api_view
from rest_framework.response import Response



data = [
    {
        "id":101,
        "name":"pani puri",
        "price":20,
        "image":"https://th.bing.com/th/id/OIP.f6jTgfn1KbGZKpCwiAyrQAHaFw?w=224&h=150&c=6&r=0&o=7&dpr=1.5&pid=1.7&rm=3"
        

    },
    {
            "id":102,
            "name":"dhahi puri",
            "price":20,
            "image":"https://www.bing.com/th/id/OIP.qahz5TkqGgxdSZYg7mvb-gHaFG?w=193&h=135&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=ImgAns&rm=2"
    
        },
        {
                "id":103,
                "name":"pani puri",
                "price":20,
                "image":"https://th.bing.com/th/id/OIP.f6jTgfn1KbGZKpCwiAyrQAHaFw?w=224&h=150&c=6&r=0&o=7&dpr=1.5&pid=1.7&rm=3"
        
            },
            {
                    "id":104,
                    "name":"pani puri",
                    "price":20,
                    "image":"https://th.bing.com/th/id/OIP.f6jTgfn1KbGZKpCwiAyrQAHaFw?w=224&h=150&c=6&r=0&o=7&dpr=1.5&pid=1.7&rm=3"
            
                },
                {
                        "id":105,
                        "name":"pani puri",
                        "price":20,
                        "image":"https://th.bing.com/th/id/OIP.f6jTgfn1KbGZKpCwiAyrQAHaFw?w=224&h=150&c=6&r=0&o=7&dpr=1.5&pid=1.7&rm=3"
                
                    },
                    {
                            "id":106,
                            "name":"pani puri",
                            "price":20,
                            "image":"https://th.bing.com/th/id/OIP.f6jTgfn1KbGZKpCwiAyrQAHaFw?w=224&h=150&c=6&r=0&o=7&dpr=1.5&pid=1.7&rm=3"
                    
                        },

    
]






@api_view(["GET"])
def getAllmenuIteams(request):
    return Response(
        {
            "stutas":"success",
            "data":data
        }
    )



@api_view(["GET"])
def getOneMenuIteam(request,id):
    dataFound=None
    for i in data:
        if i["id"]==id:
            dataFound=i
            break

    return Response(
        {
            "stutas":"success",
            "data":dataFound
        }
    )



@api_view(["POST"])
def addItems(request):
    NewItems=request.data
    NewItems["id"]=data [-1] ["id"]+1
    data.append(NewItems)




    return Response(
        {
            "stutas":"success",
            "data":data[-1]
        }
    )