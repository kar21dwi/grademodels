import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
	selector: 'app-gradesequenceinput',
	templateUrl: './gradesequenceinput.component.html',
	styleUrls: [ './gradesequenceinput.component.css' ]
})
export class GradesequenceinputComponent implements OnInit {
	constructor(private router: Router) {}

	ngOnInit() {}
}
