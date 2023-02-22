import axios from "axios"
import {urls} from "@/networking/rest/EndpointHelper.js"

import EndpointHelper from "@/networking/rest/EndpointHelper.js"

class RestHelper {
    
    constructor(){
    }

    async pingServer(){
        const response  = await axios.get("http://localhost:5000/get")
        return response
    }
}
export default RestHelper;