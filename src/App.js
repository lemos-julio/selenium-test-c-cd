import { useState } from 'react';
import Banner from './components/Banner';
import Footer from './components/footer';
import Form from './components/form';
import Team from './components/Team';

function App() {

  const teamObj = [
    {
      nome: 'Front-End',
      primaryColor: '#82CFFA',
      secondaryColor: '#E8F8FF',
    },
    {
      nome: 'Data Sciense',
      primaryColor: '#A6D157',
      secondaryColor: '#F0F8E2',
    },
    {
      nome: 'Devops',
      primaryColor: '#E06B69',
      secondaryColor: '#FDE7E8'
    },
    {
      nome: 'UX e Design',
      primaryColor: '#D86EBF',
      secondaryColor: '#FAE5F5',
    },
    {
      nome: 'Mobile',
      primaryColor: '#FEBA05',
      secondaryColor: '#FFF5D9',
    },
    {
      nome: 'Inovação e Gestão',
      primaryColor: '#FF8A29',
      secondaryColor: '#FFEEDF',
    }
  ]



  const [colaborators, setColaborators] = useState([])

  const onNewAddedColaborator = (newArrayColaborators) => {
    setColaborators([...colaborators, newArrayColaborators])
    console.log(newArrayColaborators)
  }


  return (
    <div className="App">
      <Banner />
      <Form
        teamObj={teamObj.map(time => time.nome)}
        onColaboratorSubmited={colaborador => onNewAddedColaborator(colaborador)}
      />

      {teamObj.map(team => <Team
        key={team.nome}
        teamName={team.nome}
        primaryColor={team.primaryColor}
        secondaryColor={team.secondaryColor} 
        colaborators = {colaborators.filter(colaborator => colaborator.team === team.nome)}
        />)}
        <Footer/>

    </div>
  );
}

export default App;
