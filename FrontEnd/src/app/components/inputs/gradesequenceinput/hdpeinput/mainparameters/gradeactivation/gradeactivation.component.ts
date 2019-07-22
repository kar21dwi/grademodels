import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
	selector: 'app-gradeactivation',
	templateUrl: './gradeactivation.component.html',
	styleUrls: [ './gradeactivation.component.css' ]
})
export class GradeactivationComponent implements OnInit {
	gradelist = [ 'F5400', 'P5300', 'P5200', 'P5200UV', 'B5500', 'B6401', 'HDT6', 'R5801', 'E5201S', 'E5201' ];
	flag = [ false, false, true, true, false, false, false, true, true, false ];

	@Output() tablechange = new EventEmitter<any>();

	constructor() {}

	ngOnInit() {}

	changeflag(i) {
		this.flag[i] = !this.flag[i];
		this.tablechange.emit(true);
	}
}
