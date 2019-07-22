import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { CellValueChangedEvent, GridOptions } from 'ag-grid-community';

@Component({
	selector: 'app-restartparameters',
	templateUrl: './restartparameters.component.html',
	styleUrls: [ './restartparameters.component.css' ]
})
export class RestartparametersComponent implements OnInit {
	public gridOptions: GridOptions;

	@Output() tablechange = new EventEmitter<any>();

	columnDefs = [
		{ headerName: 'Restarting Grades', field: 'RG', cellStyle: { textAlign: 'center' }, editable: false },
		{ headerName: 'Time to reach Prime Production', field: 'TPP', cellStyle: { textAlign: 'center' } },
		{ headerName: 'Avg TPH before Prime Output', field: 'ATPO', cellStyle: { textAlign: 'center' } },
		{ headerName: 'NP Generation', field: 'NP', cellStyle: { textAlign: 'center' } },
		{ headerName: 'OG Generation', field: 'OG', cellStyle: { textAlign: 'center' } },
		{ headerName: 'LG Generation', field: 'LG', cellStyle: { textAlign: 'center' } }
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

			for (let k = 1; k < 6; k++) {
				obj[this.columnDefs[k].field] = Math.floor(Math.random() * 100);
			}
			this.rowData[i] = obj;
		}
		this.rowData[0].RG = 'F5400';
		this.rowData[1].RG = 'B6401';

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
