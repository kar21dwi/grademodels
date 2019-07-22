import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
	selector: 'app-hdpeinput',
	templateUrl: './hdpeinput.component.html',
	styleUrls: [ './hdpeinput.component.css' ]
})
export class HdpeinputComponent implements OnInit {
	currentinput = 1;
	saveflag = false;

	constructor(private router: Router) {}

	ngOnInit() {}

	nextinput() {
		if (this.currentinput > 1) {
			this.currentinput = this.currentinput - 1;
		}
	}

	receivetablechangestatus($event) {
		this.saveflag = $event;
	}

	confirmtable() {}
}
