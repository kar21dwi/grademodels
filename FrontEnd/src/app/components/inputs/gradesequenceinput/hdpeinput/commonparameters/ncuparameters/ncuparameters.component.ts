import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import {
	GridOptions,
	CellValueChangedEvent,
	ModelUpdatedEvent,
	ColumnValueChangedEvent,
	CellFocusedEvent
} from 'ag-grid-community';

@Component({
	selector: 'app-ncuparameters',
	templateUrl: './ncuparameters.component.html',
	styleUrls: [ './ncuparameters.component.css' ]
})
export class NcuparametersComponent implements OnInit {
	public gridOptions: GridOptions;

	@Output() tablechange = new EventEmitter<any>();

	columnDefs = [
		{
			headerName: 'Day',
			field: 'day',
			width: 200,
			editable: false,
			cellStyle: { fontFamily: 'Open Sans Semibold' }
		},
		{ headerName: 'Day 1', field: 'day1' },
		{ headerName: 'Day 2', field: 'day2' },
		{ headerName: 'Day 3', field: 'day3' },
		{ headerName: 'Day 4', field: 'day4' },
		{ headerName: 'Day 5', field: 'day5' },
		{ headerName: 'Day 6', field: 'day6' },
		{ headerName: 'Day 7', field: 'day7' },
		{ headerName: 'Day 8', field: 'day8' },
		{ headerName: 'Day 9', field: 'day9' },
		{ headerName: 'Day 10', field: 'day10' },
		{ headerName: 'Day 11', field: 'day11' },
		{ headerName: 'Day 12', field: 'day12' },
		{ headerName: 'Day 13', field: 'day13' },
		{ headerName: 'Day 14', field: 'day14' },
		{ headerName: 'Day 15', field: 'day15' },
		{ headerName: 'Day 16', field: 'day16' },
		{ headerName: 'Day 17', field: 'day17' },
		{ headerName: 'Day 18', field: 'day18' },
		{ headerName: 'Day 19', field: 'day19' },
		{ headerName: 'Day 20', field: 'day20' },
		{ headerName: 'Day 21', field: 'day21' },
		{ headerName: 'Day 22', field: 'day22' },
		{ headerName: 'Day 23', field: 'day23' },
		{ headerName: 'Day 24', field: 'day24' },
		{ headerName: 'Day 25', field: 'day25' },
		{ headerName: 'Day 26', field: 'day26' },
		{ headerName: 'Day 27', field: 'day27' },
		{ headerName: 'Day 28', field: 'day28' },
		{ headerName: 'Day 29', field: 'day29' },
		{ headerName: 'Day 30', field: 'day30' },
		{ headerName: 'Day 31', field: 'day31' }
	];

	rowData = [];

	defaultColDef = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 100
	};

	constructor() {
		for (let i = 0; i < 3; i++) {
			const obj: any = {};

			for (let k = 1; k < 31; k++) {
				const num = Math.floor(Math.random() * 101);

				obj[this.columnDefs[k].field] = num;
			}
			this.rowData[i] = obj;
		}
		this.rowData[0].day = 'NCU Load';
		this.rowData[1].day = 'Ethylene Yield';
		this.rowData[2].day = 'Propylene Yield';

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
