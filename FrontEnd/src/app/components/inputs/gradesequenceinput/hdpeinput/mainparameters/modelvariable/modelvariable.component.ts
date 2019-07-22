import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { GridOptions, CellValueChangedEvent } from 'ag-grid-community';

@Component({
	selector: 'app-modelvariable',
	templateUrl: './modelvariable.component.html',
	styleUrls: [ './modelvariable.component.css' ]
})
export class ModelvariableComponent implements OnInit {
	public gridOptions: GridOptions;

	@Output() tablechange = new EventEmitter<any>();

	modelvariables = {
		worksheet: 'Last Running Grades',
		attributes: [
			{ header: 'Model_Type', value: 0.0 },
			{ header: 'exponential_factor', value: 0.3 },
			{ header: 'decay_factor', value: 1.0 },
			{ header: 'PLAN_DAYS', value: 30.0 },
			{ header: 'SlidingWindow', value: 8.0 },
			{ header: 'SERIES_RUN', value: 16.0 },
			{ header: 'PARALLEL_RUN', value: 5.0 }
		]
	};

	columnDefs = [];

	rowData = [];

	defaultColDef = {
		editable: this.checkEditFunction.bind(this),
		singleClickEdit: this.checkEditFunction.bind(this),
		resizable: true,
		width: 150
	};

	constructor() {
		for (let i = 0; i < 7; i++) {
			this.columnDefs[i] = {
				headerName: this.modelvariables.attributes[i].header,
				field: this.modelvariables.attributes[i].header,
				cellStyle: (params) => {
					if (params.column.colId === 'PLAN_DAYS') {
						return { color: 'lightgrey' };
					}
				}
			};
		}
		for (let k = 0; k < 2; k++) {
			const obj: any = {};
			for (let i = 0; i < 7; i++) {
				obj[this.modelvariables.attributes[i].header] = this.modelvariables.attributes[i].value;
			}

			this.rowData[k] = obj;
		}
		this.gridOptions = {
			rowData: this.rowData,
			columnDefs: this.columnDefs,
			defaultColDef: this.defaultColDef,
			suppressCellSelection: true,
			domLayout: 'autoHeight',

			onCellValueChanged: (event: CellValueChangedEvent) => {
				if (event.value !== String(event.oldValue)) {
					this.tablechange.emit(true);
				}
			}
		};
		this.gridOptions.getRowStyle = (params) => {
			if (params.node.rowIndex % 2 !== 0) {
				return { opacity: '0.5' };
			}
		};
	}

	ngOnInit() {}

	checkEditFunction(params) {
		if (params.node.childIndex === 0 && params.column.colId !== 'PLAN_DAYS') {
			return true;
		} else {
			return false;
		}
	}
}
