/** @odoo-module */
import { registry } from '@web/core/registry';
import { KpiCard } from "@custom_dashboard/components/kpi_card/kpi_card";
import { ChartRenderer } from "./chart_renderer/chart_renderer"

const { Component, useState,useRef } = owl;


export class OwlCustomDashboard extends Component {
    async setup() {
        // console.log(props)
        console.log("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    }
}

OwlCustomDashboard.template="custom_dashboard.SalesDashboard"
OwlCustomDashboard.components={ KpiCard,ChartRenderer}
registry.category('actions').add('custom_sales_dashboard', OwlCustomDashboard);

