/** @odoo-module */
import { registry } from '@web/core/registry';
const { Component, useState,useRef } = owl;
import { useService } from "@web/core/utils/hooks";

export class OwlTodoList extends Component {
    async setup() {
        this.state = useState({
            task: { name: "", color: "#FF0000", completed: false },
            taskList: [],
            isEdit: false,
            activeId: false
        });
        this.orm = useService("orm");
        this.model = "todolist.todolist";
        this.searchInput=useRef("search-input")
        await this.getAllTasks(); // Initialize tasks on setup
    }
    
    async getAllTasks() {
        try {
            this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "color", "completed"]);
            console.log(this.state.taskList,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^");
        } catch (error) {
            console.error("Error in getAllTasks():", error);
        }
    }

    addTask() {
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }
    editTask(task){
        console.log(task.id,"&&&&&&&&&&&&&&&&&&&")
        this.state.activeId = task.id
        this.state.isEdit = true
        // this.state.task = {name:task.name,color:task.color,completed:task.completed}
        this.state.task={...task}
    }

    async saveTask() {
        try {
            if(! this.state.isEdit){
                await this.orm.create(this.model, [this.state.task]);
                console.log(this.state.task); 
            }
            else{
                await this.orm.write(this.model, [ this.state.activeId],this.state.task);
            }
            await this.getAllTasks();
        } 
        catch (error) {
            console.error("Error in saveTask():", error);
        }
    }
    resetForm(){
        this.state.task={ name: "", color: "#FF0000", completed: false }
    }


    async deleteTask(task) {
        await this.orm.unlink(this.model, [task.id]);
        await this.getAllTasks()
    }


    async searchTasks() {
        try {
            const text=this.searchInput.el.value
            console.log(text,"######################")
            this.state.taskList = await this.orm.searchRead(this.model, [['name','ilike',text]], ["name", "color", "completed"]);
        } catch (error) {
            console.error("Error in searchTasks():", error);
        }
    }
    async toggleTask(e,task) {
        await this.orm.write(this.model, [task.id],{completed:e.target.checked});
        await this.getAllTasks()
    }
    async updateColor(e,task) {
        await this.orm.write(this.model, [task.id],{color:e.target.value});
        await this.getAllTasks()
    }

}

OwlTodoList.template = 'todo_list.TodoList'; 
registry.category('actions').add('custom_todo_js', OwlTodoList);
