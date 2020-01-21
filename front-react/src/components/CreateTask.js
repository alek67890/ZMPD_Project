import React from 'react'
import backend from '../apis/backend'

class TaskStatus extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            value:'',
            file:'',
            alg:'gen',
            selectValue: 'AUTOMATIC',
            timeValue: 60
          };
    }

    handleChangeSelect(event) {
        console.log(event.target.value)
        this.setState({selectValue: event.target.value});
    }

    handleChangeTime(event) {
        this.setState({timeValue: event.target.value});
    }

    sendTask(){
        try{
            this.state.file.text().then((response)=>{
                backend.post("/create", {data: response, alg: this.state.selectValue, timeValue: this.state.timeValue});
                // console.log(response);
            })
        }
        catch(e){
            console.log("No File ")
        }
    }

    handleChangeFile(event) {
        this.setState({value: event.target.value});
        this.setState({file: event.target.files[0]});
        console.log(event.target.files[0])
    }
    
    componentDidUpdate(){
        console.log(this.state)
    }


    render () {
        return <div className="ui segment">

        <div className="ui action input">
            <input type="file" placeholder="Search..." value={this.state.value} onChange={this.handleChangeFile.bind(this)} />
            <div className="ui label">Algorithm: </div>
            <select value={this.state.selectValue} onChange={this.handleChangeSelect.bind(this)} className="ui selection dropdown" id="dropmenu">
                <option value="AUTOMATIC">Automatic</option>
                <option value="SIMULATED_ANNEALING">Simulated annealing</option>
                <option value="GREEDY_DESCENT">Greedy descent</option>
                <option value="GUIDED_LOCAL_SEARCH">Guided Local Search</option>
                <option value="TABU_SEARCH">Tabu search</option>
                <option value="OBJECTIVE_TABU_SEARCH">Objective Tabu search</option>
            </select>
            <div className="ui label">Max Time: </div>
            <input type="number" name="quantity" min="1" max="1000" value={this.state.timeValue} onChange={this.handleChangeTime.bind(this)}></input>
            <div className="ui button" onClick={()=> {
                    console.log("CLIASDF");
                    this.sendTask();
                }}>Create New task</div>
        </div>


        </div>
    }
}

export default TaskStatus;



// {/* <div className='message-box'>
// <div className="ui input">
//     <input type="file" placeholder="Search..." value={this.state.value} onChange={this.handleChange.bind(this)} />
//     <select class="ui selection dropdown">
//         <option selected="" value="AUTOMATIC">Automatic</option>
//         <option value="GREEDY_DESCENT">Algorytm zachłanny</option>
//         <option value="GUIDED_LOCAL_SEARCH">GUIDED_LOCAL_SEARCH</option>
//         <option value="SIMULATED_ANNEALING">SIMULATED_ANNEALING</option>
//         <option value="TABU_SEARCH">TABU_SEARCH</option>
//         <option value="OBJECTIVE_TABU_SEARCH">OBJECTIVE_TABU_SEARCH</option>
//     </select>
// </div>

// <button className="ui basic button " onClick={()=> {
//         console.log("CLIASDF");
//         this.sendTask();
//     }}>
//     <i className="icon plus"></i>
//     Create New task
// </button>

// </div> */}
