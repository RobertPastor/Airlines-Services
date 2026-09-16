import { control } from "../og/og.es.js";

/**
 * display globe coordinates updates for each mouse move
 * 15 September 2026
 * Author : Robert PASTOR
 */

//Define custom control class
export class ogGlobeCoordinatesControl extends control.EarthCoordinates {

	constructor() {
		let options = { centerMode : false , altitudeUnit : 'm' , heightMode : 'ell' , type: 1 };
		super(options);
	}

	updateGlobeCoordinates() {
		// call protected method from inherited class
		this._refreshCoordinates();
	}

	onadd() {
		console.log("og globe coordinates update Control - onadd");
		if ( this.renderer ) {
			this.renderer.events.on("mousemove", this.updateGlobeCoordinates, this);
		}
	}

	oninit() {
		console.log("og globe coordinates update Control - oninit");
	}
}