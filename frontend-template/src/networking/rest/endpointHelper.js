
const REST_BASE_URL = "http://localhost:5000"
export const urls ={
    base : "/",
    get : '/get',
}

class EndpointHelper {
    constructor(){
    }
    validTarget(target){
        return target in urls ? true : false
    }

    buildEndpoint(route_url){
        let endpoint = REST_BASE_URL + route_url
        return endpoint
    }
}

export default EndpointHelper;