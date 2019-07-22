import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { InputsComponent } from './components/inputs/inputs.component';
import { OutputsComponent } from './components/outputs/outputs.component';
import { AdditionsComponent } from './components/additions/additions.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { HomeComponent } from './components/home/home.component';
import { GradesequenceinputComponent } from './components/inputs/gradesequenceinput/gradesequenceinput.component';
import { HdpeinputComponent } from './components/inputs/gradesequenceinput/hdpeinput/hdpeinput.component';
import { CommonparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/commonparameters/commonparameters.component';
import { MainparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/mainparameters.component';
import { OtherparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/otherparameters/otherparameters.component';
import { NcuparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/commonparameters/ncuparameters/ncuparameters.component';
import { GradeactivationComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/gradeactivation/gradeactivation.component';
import { ModelvariableComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/modelvariable/modelvariable.component';
import { DemandstockComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/demandstock/demandstock.component';
import { DemandpatternComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/demandpattern/demandpattern.component';
import { ContributionComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/contribution/contribution.component';
import { GmdemandComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/gmdemand/gmdemand.component';
import { ExecutionparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/executionparameters/executionparameters.component';
import { MinimumsalesComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/minimumsales/minimumsales.component';
import { MaximumsalesComponent } from './components/inputs/gradesequenceinput/hdpeinput/mainparameters/maximumsales/maximumsales.component';
import { RestartparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/otherparameters/restartparameters/restartparameters.component';
import { TphComponent } from './components/inputs/gradesequenceinput/hdpeinput/otherparameters/tph/tph.component';
import { LastgraderunComponent } from './components/inputs/gradesequenceinput/hdpeinput/otherparameters/lastgraderun/lastgraderun.component';
import { TransitionsComponent } from './components/inputs/gradesequenceinput/hdpeinput/otherparameters/transitions/transitions.component';
import { GradesequenceoutputComponent } from './components/outputs/gradesequenceoutput/gradesequenceoutput.component';
import { HdpeoutputComponent } from './components/outputs/gradesequenceoutput/hdpeoutput/hdpeoutput.component';
import { LldpeoutputComponent } from './components/outputs/gradesequenceoutput/lldpeoutput/lldpeoutput.component';
import { PpoutputComponent } from './components/outputs/gradesequenceoutput/ppoutput/ppoutput.component';
import { GradeadditionComponent } from './components/additions/gradeaddition/gradeaddition.component';
import { HdpeadditionComponent } from './components/additions/gradeaddition/hdpeaddition/hdpeaddition.component';
import { LldpeadditionComponent } from './components/additions/gradeaddition/lldpeaddition/lldpeaddition.component';
import { PpadditionComponent } from './components/additions/gradeaddition/ppaddition/ppaddition.component';
import { PropertyadditionComponent } from './components/additions/propertyaddition/propertyaddition.component';
import { ContributiondditionComponent } from './components/additions/propertyaddition/contributionddition/contributionddition.component';
import { MinimumsalesadditionComponent } from './components/additions/propertyaddition/minimumsalesaddition/minimumsalesaddition.component';
import { MaximumsalesadditionComponent } from './components/additions/propertyaddition/maximumsalesaddition/maximumsalesaddition.component';
import { GmdemandadditionComponent } from './components/additions/propertyaddition/gmdemandaddition/gmdemandaddition.component';
import { RestartparametersadditionComponent } from './components/additions/propertyaddition/restartparametersaddition/restartparametersaddition.component';
import { TransitionsadditionComponent } from './components/additions/propertyaddition/transitionsaddition/transitionsaddition.component';
import { AgGridModule } from 'ag-grid-angular';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';

@NgModule({
	declarations: [
		AppComponent,
		InputsComponent,
		OutputsComponent,
		AdditionsComponent,
		NavigationComponent,
		HomeComponent,
		GradesequenceinputComponent,
		HdpeinputComponent,
		CommonparametersComponent,
		MainparametersComponent,
		OtherparametersComponent,
		NcuparametersComponent,
		GradeactivationComponent,
		ModelvariableComponent,
		DemandstockComponent,
		DemandpatternComponent,
		ContributionComponent,
		GmdemandComponent,
		ExecutionparametersComponent,
		MinimumsalesComponent,
		MaximumsalesComponent,
		RestartparametersComponent,
		TphComponent,
		LastgraderunComponent,
		TransitionsComponent,
		GradesequenceoutputComponent,
		HdpeoutputComponent,
		LldpeoutputComponent,
		PpoutputComponent,
		GradeadditionComponent,
		HdpeadditionComponent,
		LldpeadditionComponent,
		PpadditionComponent,
		PropertyadditionComponent,
		ContributiondditionComponent,
		MinimumsalesadditionComponent,
		MaximumsalesadditionComponent,
		GmdemandadditionComponent,
		RestartparametersadditionComponent,
		TransitionsadditionComponent
	],
	imports: [ BrowserModule, AppRoutingModule, AgGridModule.withComponents([ AppComponent ]), MatSlideToggleModule ],
	providers: [],

	bootstrap: [ AppComponent ]
})
export class AppModule {}
