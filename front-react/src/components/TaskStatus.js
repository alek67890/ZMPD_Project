import React from 'react'
// import ReactDOM from 'react-dom'
import { Line } from 'rc-progress';
import PlotCompoment from './PlotCompoment';

class TaskStatus extends React.Component {

  render () {
    let plot =''
    if (this.props.status === 'finished'){
      plot = <div>
        <PlotCompoment name={this.props.name} points={JSON.parse(this.props.points)} routes_plot={JSON.parse(this.props.routes_plot)}/>
        total_load = {this.props.total_load}<br/>
        total_distance={this.props.total_distance}<br/>
      </div>
      
    }
    let alg = ''
    switch (this.props.alg) {
      case 'AUTOMATIC':
        alg = "Automatic";
        break;
      case 'SIMULATED_ANNEALING':
        alg = "Simulated annealing";
        break;
      case 'GREEDY_DESCENT':
        alg = "Greedy descent";
        break;
      case 'GUIDED_LOCAL_SEARCH':
        alg = "Guided Local Search";
        break;
      case 'TABU_SEARCH':
        alg = "Tabu search";
        break;
      case 'OBJECTIVE_TABU_SEARCH':
        alg = "Objective Tabu search";
        break;
      default:
        alg = 'Unknown'
    }
    
    return <div className="ui segment">
        <div className='message-box'>
        {this.props.name} <br/>
        Algorithm used: {alg} <br/>
        Progress : {this.props.progress}%
        <Line percent={this.props.progress} strokeWidth="4" strokeColor="blue" />
        Current status : {this.props.status}
        {plot}
      </div>
    </div>
  }
}

export default TaskStatus;