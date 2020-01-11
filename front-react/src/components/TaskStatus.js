import React from 'react'
// import ReactDOM from 'react-dom'
import { Line } from 'rc-progress';

class TaskStatus extends React.Component {


  render () {
    return <div className="ui segment">
        <div className='message-box'>
        Hello World {this.props.name}
        <br/> Progress : {this.props.progress}%
        <Line percent={this.props.progress} strokeWidth="4" strokeColor="blue" />
        Current status : {this.props.status}
        {/* {JSON.stringify(this.props.output)} */}
      </div>
    </div>
  }
}

export default TaskStatus;