import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { CellValueChangedEvent, GridOptions } from 'ag-grid-community';

@Component({
	selector: 'app-executionparameters',
	templateUrl: './executionparameters.component.html',
	styleUrls: [ './executionparameters.component.css' ]
})
export class ExecutionparametersComponent implements OnInit {
	public gridOptions: GridOptions;

	@Output() tablechange = new EventEmitter<any>();

	columnDefs = [
		{
			headerName: 'Trains',
			field: 'trains',
			editable: false,
			cellStyle: { fontFamily: 'Open Sans Semibold' }
		},
		{ headerName: 'Execution Start Date', field: 'execstartdate', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Execution Start Time', field: 'execstarttime', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Execution Duration', field: 'execduration', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Planned Maintenance Start Day', field: 'pmsd', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Planned Maintenance Start Hour', field: 'pmsh', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Planned Maintenance Duration', field: 'pmd', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Initial Maintenance Duration', field: 'imd', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Allowable Days', field: 'allowdays', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Allowable Hours', field: 'allowhours', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Difference in Days Maintenance', field: 'ddm', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Difference in Hours Maintenance', field: 'dhm', cellStyle: { textAlign: 'center' } }
	];

	rowData = [];

	defaultColDef = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 150
	};

	constructor() {
		for (let i = 0; i < 2; i++) {
			const obj: any = {};

			obj[this.columnDefs[0].field] = 'Train ' + String(i + 1);
			obj[this.columnDefs[1].field] = '08-08-2018';
			obj[this.columnDefs[3].field] = '30';
			this.rowData[i] = obj;
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
	}

	ngOnInit() {}
}
