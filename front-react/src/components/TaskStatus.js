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
    
// {JSON.parse(this.props.routes_plot)}

    return <div className="ui segment">
        <div className='message-box'>
        {this.props.name}
        <br/> Progress : {this.props.progress}%
        <Line percent={this.props.progress} strokeWidth="4" strokeColor="blue" />
        Current status : {this.props.status}
        {plot}
      </div>
    </div>
  }
}

export default TaskStatus;