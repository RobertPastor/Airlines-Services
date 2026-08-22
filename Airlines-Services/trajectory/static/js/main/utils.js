/*
* Assumption : a route as a string contains
* 1) the Departure airport ICAO code
* 2) a DASH '-' separator
* 3) the destination airport ICAO code
*/
export class Route {
	
	constructor(routeAsString) {
		this.routeAsString = routeAsString;
        this.Adep = "";
        this.Ades = "";
        if ( this.check() == true ) {
            // route contains a DASH separator
            let arr = routeAsString.split("-");
		    this.Adep = arr[1];
		    this.Ades = arr[2];
        } else {
            console.error( "Route as string does not contains a DASH separator");
        }
	}

    check() {
        let arr = this.routeAsString.split("-");
        if ( ( this.routeAsString.indexOf("-") != -1 ) && Array.isArray(arr) && (arr.length > 1) ) {
            return true;
        } else {
            return false;
        }
    }

    getAdep() {
        return this.Adep;
    }
    getAdes() {
        return this.Ades;
    }

}