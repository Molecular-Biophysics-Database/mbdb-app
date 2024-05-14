import FormWrapper from '../../../buildingBlocks/FormWrapper';
import Homogeneity from './homogeneity/Homogeneity';
import Identity from './identity/Identity';
import Purity from './purity/Purity';

function QualityControls( { name, colorSchema } ) {

  return (
    <>
        <FormWrapper
            headline='Quality controls'
            colorSchema={colorSchema}
            tooltip='Information about if and how quality control of the molecular assembly was performed'
        >
            <div className='mb-3 -mt-3'>
                <Purity name={name} colorSchema={colorSchema === 'light' ? '' : 'light'} />
            </div>
            <div className='mb-3'>
                <Identity name={name} colorSchema={colorSchema === 'light' ? '' : 'light'} />
            </div>
            <div>
                <Homogeneity name={name} colorSchema={colorSchema === 'light' ? '' : 'light'} />
            </div>
        </FormWrapper>
    </>
  );
}

export default QualityControls;
