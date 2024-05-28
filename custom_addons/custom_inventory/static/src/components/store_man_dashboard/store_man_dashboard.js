// /** @odoo-module */
// import { registry } from '@web/core/registry';
// import { KpiCard } from "@custom_inventory/components/kpi_card/kpi_card";
// import { ChartRenderer } from "./chart_renderer/chart_renderer";

// const { Component, useState } = owl;

// export class StoreManDashboard extends Component {
//     async setup() {
//         this.state = useState({
//             inbound_stock: [],
//             assigned_stock: [],
//             proformas: [],
//         });

//         await this.fetchDashboardData();
//     }

//     async fetchDashboardData() {
//         const response = await fetch('/landing_page');
//         const data = await response.json();
//         this.state.inbound_stock = data.inbound_stock;
//         this.state.assigned_stock = data.assigned_stock;
//         this.state.proformas = data.proformas;
//     }
// }

// StoreManDashboard.template = "custom_inventory.StoreManDashboard";
// StoreManDashboard.components = { KpiCard, ChartRenderer };

// registry.category('actions').add('custom_store_manager_dashboard', StoreManDashboard);
