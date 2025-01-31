from django.shortcuts import render
from .forms import ImageUploadForm
from django.core.files.storage import FileSystemStorage

from . import Class_model
def acne_desc():
    text = '''Acne is a common skin condition that primarily affects individuals during adolescence but can persist into adulthood. Here’s a detailed description based on the information gathered:
        
<h4>What is Acne?</h4>
Acne, also known as acne vulgaris, is a long-term skin condition characterized by the presence of pimples, blackheads, and whiteheads. It occurs when hair follicles become clogged with oil (sebum) and dead skin cells. This blockage can lead to various types of lesions on the skin, including:

- Blackheads: Open comedones that appear dark due to oxidation.
- Whiteheads: Closed comedones that appear as small, flesh-colored bumps.
- Papules: Small, raised red bumps that are often inflamed.
- Pustules: Similar to papules but filled with pus.
- Nodules: Large, painful lumps beneath the skin's surface.
- Cysts: Deep, pus-filled lesions that can cause scarring.

<h4>Causes of Acne</h4>
The primary causes of acne include:
- Excess Sebum Production: Sebaceous glands produce too much oil, which mixes with dead skin cells and clogs hair follicles.
- Hormonal Changes: Androgens, hormones that increase during puberty, stimulate sebaceous glands and lead to increased oil production.
- Bacterial Growth: The bacterium Cutibacterium acnes (formerly Propionibacterium acnes) can proliferate in clogged pores, leading to inflammation.
- Genetic Factors: A family history of acne can increase susceptibility.
- Skin Cell Turnover: Abnormal shedding of skin cells can contribute to pore blockage.

<h4>Symptoms</h4>
Acne typically manifests as:
- Oily skin
- Blackheads and whiteheads
- Red, inflamed bumps (papules)
- Pus-filled lesions (pustules)
- Painful lumps under the skin (nodules and cysts)
- Scarring or post-inflammatory hyperpigmentation after lesions heal

<h4>Common Areas Affected</h4>
Acne most commonly appears on:
- The face
- Neck
- Shoulders
- Upper back
- Chest

<h4>Risk Factors</h4>
While acne is most prevalent among teenagers, it can affect individuals of all ages, including infants and adults. The following factors may exacerbate acne:
- Hormonal fluctuations (e.g., menstrual cycles)
- Certain medications (e.g., corticosteroids)
- Diets high in refined sugars or dairy products (though this connection is controversial)
- Stress
- Psychological Impact
- Acne can have significant psychological effects, including anxiety, reduced self-esteem, and depression. The visibility of acne lesions can lead to social withdrawal and emotional distress.


<h4>Treatment Options</h4>
Effective treatments for acne include:
<h5>Topical Treatments:</h5>
- Benzoyl peroxide
- Salicylic acid
- Retinoids (e.g., tretinoin)
<h5>Oral Medications:</h5>
- Antibiotics (for inflammatory acne)
- Hormonal treatments (like birth control pills for women)
- Isotretinoin (for severe cases)
<h5>Lifestyle Changes:</h5>
- Maintaining a regular skincare routine
- Avoiding heavy makeup
- Eating a balanced diet
<h5>Professional Procedures:</h5>
- Chemical peels
- Laser therapy
- Drainage and extraction for cysts

<h4>Conclusion</h4>
Acne is a multifactorial condition that requires a comprehensive approach for effective management. Understanding its causes and manifestations can help individuals seek appropriate treatment and mitigate its psychological impact. If self-care measures do not improve the condition, consulting a healthcare provider or dermatologist is recommended for tailored treatment options.
For further information on acne management and treatment options, consult healthcare professionals or reliable medical resources.'''
    return text

def hyperpigmentation_desc():
    text = ''' <h3>Hyperpigmentation is a common skin condition characterized by dark patches or spots on the skin, resulting from an excess production of melanin, the pigment responsible for skin color. This condition can affect individuals of all skin types but is particularly noticeable in those with darker skin tones.</h3>

<h4>Causes of Hyperpigmentation</h4>
- Sun Exposure: Prolonged exposure to sunlight is the most significant factor leading to hyperpigmentation. UV rays stimulate melanin production as a protective response, which can result in dark spots, commonly referred to as sunspots or age spots.
- Hormonal Changes: Conditions such as pregnancy can lead to melasma, a type of hyperpigmentation that typically appears on the face and is influenced by hormonal fluctuations.
- Post-Inflammatory Hyperpigmentation: This occurs following skin trauma or inflammation, such as acne, cuts, or burns. The affected areas may darken as the skin heals.
- Medications: Certain drugs, including some chemotherapy agents and oral contraceptives, can cause hyperpigmentation as a side effect.
- Genetic Factors: Some individuals may be genetically predisposed to develop hyperpigmented areas on their skin.
- Underlying Health Conditions: Conditions like Addison's disease can lead to increased melanin production and resultant hyperpigmentation.</p>

<h4>Types of Hyperpigmentation</h4>
- Melasma: Often triggered by hormonal changes, it typically appears on the face, particularly on the cheeks, forehead, and upper lip.
- Sunspots (Solar Lentigines): These are flat brown spots that develop due to sun exposure over time and are commonly found on sun-exposed areas like the face and hands.
- Post-Inflammatory Hyperpigmentation:This type occurs after an injury or inflammation of the skin, often seen in acne scars.


<h4>Treatment Options</h4>
<h5>Topical Treatments:</h5>
- Hydroquinone: A skin-lightening agent that reduces melanin production.
- Retinoids: Help in cell turnover and reduce pigmentation.
- Vitamin C: An antioxidant that can brighten the skin and reduce dark spots.
- Azelaic Acid and Kojic Acid: Both can inhibit melanin production and lighten hyperpigmented areas.

<h5>Procedures:</h5>
- Chemical Peels: Remove the outer layer of skin to promote new skin growth.
- Laser Therapy: Targets pigmented areas without damaging surrounding skin.
- Microdermabrasion: Exfoliates the skin to improve its texture and tone.

<h5>Preventive Measures:</h5> 
- Regular use of sunscreen is crucial to prevent worsening of hyperpigmentation caused by sun exposure.
- Protective clothing and avoiding peak sun hours can also help mitigate risks.


<h4>Conclusion</h4>
While hyperpigmentation is generally not harmful, it can cause emotional distress due to its appearance. Understanding its causes and treatment options is essential for effective management. If you experience significant changes in your skin pigmentation or have concerns about specific spots, consulting a dermatologist for personalized advice and treatment options is recommended.'''
    return text


def Nail_psoriasis_desc():
    text=''' Nail psoriasis is a specific manifestation of psoriasis that affects the nails on both fingers and toes, leading to various changes in their appearance and texture. Below is a detailed description of nail psoriasis, including its symptoms, causes, treatment options, and prevention strategies.
Nail psoriasis is an autoimmune condition characterized by rapid skin cell growth, which can lead to inflammation and changes in the nails. It often occurs in individuals who have psoriasis on their skin but can also appear independently.

<h4>Symptoms</h4>
Common symptoms of nail psoriasis include:
- Color Changes: Nails may turn white, yellow, or brown. Small red or white spots may also appear underneath the nails.
- Pitting: Small pinprick holes or dents on the surface of the nails.
- Thickening: Nails may become thickened and brittle, making them prone to breakage.
- Separation: The nail may loosen or separate from the nail bed, sometimes causing pain.
- Debris Buildup: Chalky white material can accumulate under the nail, leading to discomfort.
These changes can make it difficult to perform daily tasks and may cause tenderness or pain in the affected areas.

<h4>Causes</h4>
Nail psoriasis is primarily linked to genetic factors and immune system dysfunction. It is more common in individuals with a history of psoriasis elsewhere on their body. Approximately 50% of people with psoriasis will experience nail involvement at some point.

<h4>Treatment Options</h4>
Treatment for nail psoriasis can vary based on severity and may include:
- Topical Treatments:
- Corticosteroids: Creams or ointments applied directly to the nails and surrounding skin.
- Vitamin D Analogues: These help slow down skin cell growth.
- Retinoids: Topical retinoids can also be beneficial.
- Systemic Medications: Medications that affect the entire body, such as biologics (e.g., TNF-alpha inhibitors) and systemic retinoids, may be prescribed for more severe cases.
- Phototherapy: Ultraviolet (UV) light treatments can help reduce symptoms by targeting the immune response.
- Corticosteroid Injections: Injections under the nail can provide relief from inflammation and pain.
- Cosmetic Solutions: Nail varnishes or artificial nails can improve appearance and protect against further damage.

<h4>Prevention Strategies</h4>
To help manage and prevent worsening of nail psoriasis:
- Keep nails trimmed short.
- Use a nail file to smooth edges.
- Wear gloves during cleaning or other activities that may damage nails.
- Moisturize nails and cuticles regularly.
- Choose comfortable footwear that allows room for toes.

<h4>Conclusion</h4>
Nail psoriasis can significantly impact quality of life due to its physical effects and associated discomfort. While there is no cure, various treatment options are available to manage symptoms effectively. It's essential for individuals experiencing symptoms to consult a healthcare provider for an accurate diagnosis and personalized treatment plan. Regular monitoring and good nail care practices can also help mitigate symptoms and improve nail health over time.'''
    return text

def SJS_TEN_desc():
    text= ''' Stevens-Johnson Syndrome (SJS) and Toxic Epidermal Necrolysis (TEN) are severe, life-threatening skin conditions characterized by extensive skin damage and mucosal involvement. They are often drug-induced and can lead to significant morbidity and mortality.

<h4>Classification</h4>
- SJS: Involves less than 10% of the body surface area (BSA).
- SJS-TEN Overlap: Involves 10-30% of BSA.
- TEN: Involves more than 30% of BSA.

<h4>Symptoms</h4>
Early symptoms typically include:
- Fever
- Flu-like symptoms
- Painful skin blisters and peeling
- Involvement of mucous membranes (mouth, eyes, genitalia)
As the condition progresses, patients may experience painful raw areas on the skin and mucous membranes.

<h4>Causes</h4>
The primary triggers for SJS and TEN include:
<h5>Medications-  Certain drugs are commonly associated with these syndromes, including:</h5>
- Antiepileptics (e.g., lamotrigine, carbamazepine)
- Antibiotics (e.g., sulfonamides)
- Allopurinol
<h5>Infections:</h5> Some infections, such as those caused by Mycoplasma pneumoniae or cytomegalovirus, can also lead to SJS/TEN.
<h5>Unknown Factors:</h5> In some cases, the cause remains unidentified.

<h4>Risk Factors</h4>
Individuals at higher risk include those with:
- HIV/AIDS
- Systemic lupus erythematosus
- Certain genetic predispositions

<h4>Diagnosis
Diagnosis is primarily clinical and based on the extent of skin involvement. A skin biopsy may be performed but is not always necessary. A positive Nikolsky's sign (skin peeling upon gentle pressure) can aid in diagnosis.

<h4>Complications</h4>
Complications from SJS/TEN can be severe and include:
- Dehydration
- Sepsis
- Pneumonia
- Multiple organ failure
The mortality rate for SJS is approximately 5–10%, while TEN has a higher mortality rate of 15–20%, especially in elderly or immunocompromised patients.

<h4>Treatment</h4>
- Management typically requires hospitalization in specialized units such as burn units or intensive care. Treatment strategies include:
- Immediate cessation of the offending drug
- Supportive care for hydration and nutrition

<h4>Pain management</h4>
- Use of medications like corticosteroids, intravenous immunoglobulins, and antibiotics to manage secondary infections
- Prognosis
Recovery can take weeks to months, with skin regrowth occurring over two to three weeks. However, complete recovery may require much longer, depending on the severity of the condition.

<h4>Conclusion</h4>
SJS and TEN are serious medical emergencies that necessitate prompt recognition and management. Ongoing research aims to improve understanding and treatment outcomes for these conditions through multidisciplinary collaboration across various medical fields.'''
    return text

def Vitiligo_desc():
    text = ''' Vitiligo is a chronic autoimmune disorder characterized by the loss of skin pigment, resulting in white patches on various parts of the body. This condition occurs when melanocytes, the cells responsible for producing melanin (the pigment that gives skin its color), are attacked and destroyed by the body's immune system.

<h4>Nature of the Condition/h4>
Vitiligo is not contagious or life-threatening but can significantly impact an individual's self-esteem and emotional well-being. The white patches typically appear symmetrically on both sides of the body, such as on hands, knees, and face, although they can also develop in isolated areas.</p>

<h4>Types/h4>
- Non-segmental Vitiligo: The most common form, accounting for about 90% of cases, where patches appear symmetrically.
- Segmental Vitiligo: Less common and usually localized to one side of the body. It often starts at a young age and may stop progressing after a certain period.

<h4>Symptoms/h4>
Depigmentation: The primary symptom is the development of white patches on the skin, which can vary in size and shape.

<h4>Affected Areas/h4>
Commonly affected areas include:
- Skin on hands, feet, arms, face, and around body openings.
- Hair may turn white in areas where skin loses pigment.
- Mucous membranes (inside the mouth or nose) can also be affected.
- Associated Conditions: People with vitiligo may experience low self-esteem or depression due to their appearance. Additionally, they may be at higher risk for other autoimmune diseases such as thyroid disease and type 1 diabetes.

<h4>Causes/h4>
- The exact cause of vitiligo remains unclear, but it is believed to be an autoimmune response where the immune system mistakenly attacks melanocytes. Factors that may trigger or worsen vitiligo include:
- Genetic predisposition (family history).
- Environmental factors such as sunburn or exposure to certain chemicals.
- Emotional stress.

<h4>Diagnosis/h4>
Diagnosis typically involves a physical examination of the skin and medical history. In some cases, a dermatologist may perform a skin biopsy or blood tests to rule out other conditions.

<h4>Treatment Options/h4>
While there is no cure for vitiligo, several treatment options aim to restore skin color or even out skin tone:
- Phototherapy: Controlled exposure to ultraviolet light can help repigment the skin.
- Topical Treatments: Steroid creams can suppress immune activity in the skin.
- Laser Therapy: Effective for smaller areas of depigmentation.
- Surgical Options: Skin grafting techniques may be considered for stable vitiligo.
- Depigmentation: In cases where vitiligo covers large areas, bleaching unaffected skin to match the lighter patches may be an option.

<h4>Emotional Support/h4>
The psychological impact of vitiligo can be significant. Support from friends, family, or counseling services can help individuals cope with the emotional challenges associated with this condition.

<h4>Conclusion</h4>
Vitiligo is a complex condition that affects individuals differently. While it does not pose physical health risks, its effects on appearance and mental health can be profound. Ongoing research is aimed at finding more effective treatments and understanding the underlying mechanisms of this disorder.'''
    return text


def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)
            data_directory = 'Health_website/image_process/image_classifier.h5'
            temp_result = Class_model.run_model(data_directory, fs.path(filename))  # Calling the function from Class_model.py.
            result = "Cannot detect"
            if temp_result == "acne":
                result = acne_desc()
            elif temp_result == "hyperpigmentation":
                result = hyperpigmentation_desc()
            elif temp_result == "Nail_psoriasis":
                result = Nail_psoriasis_desc()
            elif temp_result == "SJS-TEN":
                result = SJS_TEN_desc()
            elif temp_result == "Vitiligo":
                result = Vitiligo_desc()

            return render(request, 'image_process/result.html', {
                'uploaded_file_url': uploaded_file_url,
                'result': result,
            })
    else:
        form = ImageUploadForm()
    return render(request, 'image_process/upload.html', {'form': form})

def Home(request):
        return render(request, 'image_process/Home.html')

def Acne(request):
    return render(request, 'image_process/Acne.html')
def hyperpigmentation(request):
    return render(request, 'image_process/hyperpigmentation.html')
def Nail_p(request):
    return render(request, 'image_process/Nail_p.html')
def Sjs(request):
    return render(request, 'image_process/Sjs.html')
def Vitiligo(request):
    return render(request, 'image_process/Vitiligo.html')
def Affect(request):
    return render(request, 'image_process/Affect.html')