import "./fieldText.css"



const FieldText = (props) => {

    
    const onText = (event) => {
        props.onChange(event.target.value)
    }

    return (
        <div  className="filedText" >
            <label>{props.label}</label>
            <input value={props.value}  onChange={onText} placeholder={props.placeholder} />
        </div>

    );
}


export default FieldText