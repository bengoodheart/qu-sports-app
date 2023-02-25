import axios from "axios"
import {urls} from "@/networking/rest/EndpointHelper.js"

import EndpointHelper from "@/networking/rest/EndpointHelper.js"

const ep = new EndpointHelper();

class RestHelper {
    
    constructor(){
    }

    async pingServer(){
        let endpoint =  ep.buildEndpoint(urls.base)
        const response  = await axios.get(endpoint)
        if (response.status != 200){
            return "Error on ping"
        } 
        if (response.status == 200){
            return "alive"
        }
    }

    async getAllPosts(){
        let endpoint = ep.buildEndpoint(urls.get)
        const response = await axios.get(endpoint)
        return response.data
    }
}
export default RestHelper;