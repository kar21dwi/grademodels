import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { CellValueChangedEvent, GridOptions } from 'ag-grid-community';

@Component({
	selector: 'app-lastgraderun',
	templateUrl: './lastgraderun.component.html',
	styleUrls: [ './lastgraderun.component.css' ]
})
export class LastgraderunComponent implements OnInit {
	@Output() tablechange = new EventEmitter<any>();
	/*-------------------------------table1 data------------------------------------*/
	public gridOptions1: GridOptions;

	columnDefs1 = [
		{ headerName: 'Train', field: 'train', editable: false },
		{ headerName: 'Grade Code', field: 'gradecode' },
		{ headerName: 'Last Running Grade', field: 'grade' },
		{
			headerName: 'Production Hours completed Last running Grade',
			field: 'PHCLG'
		},
		{
			headerName: 'Production Hours completed for series/parallel grades',
			field: 'PHCSP'
		},
		{
			headerName: 'Production Hours completed for Last running Family',
			field: 'PHCLF'
		}
	];

	rowData1 = [];

	defaultColDef1 = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 200
	};

	/*-------------------------------table2 data------------------------------------*/
	public gridOptions2: GridOptions;

	columnDefs2 = [
		{ headerName: 'Train', field: 'train', editable: false },
		{ headerName: 'SI No', field: 'slNo' },
		{ headerName: 'Transition ID', field: 'transitionId' },
		{ headerName: 'From Grade', field: 'from' },
		{ headerName: 'To Grade', field: 'to' },
		{ headerName: 'Production Hours completed for Transition', field: 'PHCT' }
	];

	rowData2 = [];

	defaultColDef2 = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 150
	};

	/*-------------------------------table3 data------------------------------------*/
	public gridOptions3: GridOptions;

	columnDefs3 = [
		{ headerName: 'Train', field: 'train', editable: false },
		{ headerName: 'SI No', field: 'slNo' },
		{ headerName: 'Remaining Hours of Maintenance', field: 'RHM' }
	];

	rowData3 = [];

	defaultColDef3 = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 150
	};

	/*-------------------------------table4 data------------------------------------*/
	public gridOptions4: GridOptions;

	columnDefs4 = [
		{ headerName: 'Train', field: 'train', editable: false },
		{ headerName: 'SI No', field: 'slNo' },
		{ headerName: 'Restart Grade', field: 'RG' },
		{ headerName: 'Remaining time required to reach Max TPH', field: 'RTMTPH' }
	];

	rowData4 = [];

	defaultColDef4 = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 150
	};

	constructor() {
		/*-------------------------------table1------------------------------------*/
		for (let i = 0; i < 2; i++) {
			const obj: any = {};
			obj[this.columnDefs1[0].field] = i + 1;
			for (let k = 3; k < 6; k++) {
				obj[this.columnDefs1[k].field] = Math.floor(Math.random() * 100);
			}
			this.rowData1[i] = obj;
		}
		this.rowData1[0].grade = 'B6401';
		this.rowData1[1].grade = 'F5400';
		this.rowData1[0].gradecode = '5';
		this.rowData1[1].gradecode = '0';

		this.gridOptions1 = {
			rowData: this.rowData1,
			columnDefs: this.columnDefs1,
			defaultColDef: this.defaultColDef1,
			suppressCellSelection: true,
			domLayout: 'autoHeight',

			onCellValueChanged: (event: CellValueChangedEvent) => {
				if (event.value !== String(event.oldValue)) {
					this.tablechange.emit(true);
				}
			}
		};
		/*-------------------------------table2------------------------------------*/
		for (let i = 0; i < 2; i++) {
			const obj: any = {};

			obj[this.columnDefs2[0].field] = i + 1;

			this.rowData2[i] = obj;
		}

		this.gridOptions2 = {
			rowData: this.rowData2,
			columnDefs: this.columnDefs2,
			defaultColDef: this.defaultColDef2,
			suppressCellSelection: true,
			domLayout: 'autoHeight',

			onCellValueChanged: (event: CellValueChangedEvent) => {
				if (event.value !== String(event.oldValue)) {
					this.tablechange.emit(true);
				}
			}
		};
		/*-------------------------------table3------------------------------------*/
		for (let i = 0; i < 2; i++) {
			const obj: any = {};

			obj[this.columnDefs3[0].field] = i + 1;

			this.rowData3[i] = obj;
		}

		this.gridOptions3 = {
			rowData: this.rowData3,
			columnDefs: this.columnDefs3,
			defaultColDef: this.defaultColDef3,
			suppressCellSelection: true,
			domLayout: 'autoHeight',

			onCellValueChanged: (event: CellValueChangedEvent) => {
				if (event.value !== String(event.oldValue)) {
					this.tablechange.emit(true);
				}
			}
		};
		/*-------------------------------table4------------------------------------*/
		for (let i = 0; i < 2; i++) {
			const obj: any = {};

			obj[this.columnDefs4[0].field] = i + 1;

			this.rowData4[i] = obj;
		}

		this.gridOptions4 = {
			rowData: this.rowData4,
			columnDefs: this.columnDefs4,
			defaultColDef: this.defaultColDef4,
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
