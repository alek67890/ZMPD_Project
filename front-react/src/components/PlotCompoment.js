import React from 'react'
// import ReactDOM from 'react-dom'
import Plotly from 'plotly.js-basic-dist'


import createPlotlyComponent from 'react-plotly.js/factory';
const Plot = createPlotlyComponent(Plotly); 

class PlotCompoment extends React.Component {
  constructor(props){
    super(props);

    this.state = {
      data : [],
      };
}

componentDidMount(){
  let temp = [[145.0, 215.0],    [151.0, 264.0],   [159.0, 261.0],    [130.0, 254.0],    [128.0, 252.0],    [163.0, 247.0],   [146.0, 246.0],    [161.0, 242.0],    [142.0, 239.0],    [163.0, 236.0],    [148.0, 232.0],    [128.0, 231.0],    [156.0, 217.0],    [129.0, 214.0],    [146.0, 208.0],    [164.0, 208.0],    [141.0, 206.0],    [147.0, 193.0],    [164.0, 193.0],    [129.0, 189.0],    [155.0, 185.0],    [139.0, 182.0]]

  let routes = [[[145.0, 163.0, 161.0, 146.0, 130.0, 128.0, 128.0, 145.0],
  [215.0, 236.0, 242.0, 246.0, 254.0, 252.0, 231.0, 215.0]],
 [[145.0, 148.0, 163.0, 159.0, 151.0, 142.0, 129.0, 145.0],
  [215.0, 232.0, 247.0, 261.0, 264.0, 239.0, 214.0, 215.0]],
 [[145.0, 156.0, 164.0, 147.0, 129.0, 145.0],
  [215.0, 217.0, 208.0, 193.0, 189.0, 215.0]],
 [[145.0, 146.0, 164.0, 155.0, 139.0, 141.0, 145.0],
  [215.0, 208.0, 193.0, 185.0, 182.0, 206.0, 215.0]]]

  routes = routes.map((route) => {
    return {
      x: route[0],
      y: route[1],
      mode: 'lines',
      type: 'scatter'
    }
  })

  let trace1 = {
    x: temp.map((item)=>item[0]),
    y: temp.map((item)=>item[1]),
    mode: 'markers',
    type: 'scatter'
  };

  let data = [trace1, ...routes]
  console.log(data)
  this.setState({data : data}) 

}
  render () {

    console.log(this.state.data)
    return <div className="ui segment">
        <div className='message-box'>
          Hello World 
          <br/>

          <Plot
            data={this.state.data}
            layout={ {width: 600, height: 400, title: 'A Fancy Plot'} }
          />


          
      </div>
    </div>
  }
}

export default PlotCompoment;