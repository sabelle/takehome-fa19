import React, { Component } from 'react'

class Counter extends Component {
  // YOUR CODE GOES BELOW
  constructor(props) {
    super(props);
    this.state = {count: 0}
  }
  // count = 0;

  incrClick = () => {
    //count: this.state.count + this.props.increment,
    count++;
    alert('count has been incremented')
  }
  decrClick = () => {
    count--;
    alert('count has been decremented')
  }

  render() {
    return (
      <div>
        <label>{count}</label>
        <button onClick={this.incrClick}>increment</button>
        <button onClick={this.decrClick}>decrement</button>
      <div/>
    )
  }
}

export default Counter
