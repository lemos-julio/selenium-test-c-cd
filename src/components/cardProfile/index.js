import './cardProfile.css'

const Profile = (props) =>{
    return(
        <div className='colaborador'>
            <div className='cabecalho' style={{backgroundColor: props.backgroundColor}}>
                <img src={props.image} alt=''/>
            </div>
            <div className='rodape'>
                <h4>{props.name}</h4>
                <h5>{props.cargo}</h5>
            </div>
        </div>
    )
}

export default Profile