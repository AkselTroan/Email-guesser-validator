def generate_emails(firstname, lastname, domain, year):
    emails = []
    first = firstname.lower()
    last = lastname.lower()
    f = first[0]
    l = last[0]
    fi = first[:1]
    la = last[:1]
    fir = first[:2]
    las = last[:2]
    er = year[2:]
    

    emails.append(f'{first}@{domain}')
    emails.append(f'{first}{last}@{domain}')
    emails.append(f'{first}.{last}@{domain}')
    emails.append(f'{first}-{last}@{domain}')
    emails.append(f'{first}_{last}@{domain}')

    emails.append(f'{last}@{domain}')

    emails.append(f'{f}{last}@{domain}')
    emails.append(f'{f}.{last}@{domain}')
    emails.append(f'{f}-{last}@{domain}')
    emails.append(f'{f}_{last}@{domain}')

    emails.append(f'{first}{l}@{domain}')
    emails.append(f'{first}.{l}@{domain}')
    emails.append(f'{first}-{l}@{domain}')
    emails.append(f'{first}_{l}@{domain}')


    emails.append(f'{last}{f}@{domain}')
    emails.append(f'{last}.{f}@{domain}')
    emails.append(f'{last}-{f}@{domain}')
    emails.append(f'{last}_{f}@{domain}')

    emails.append(f'{fir}{las}@{domain}')
    emails.append(f'{fir}.{las}@{domain}')
    emails.append(f'{fir}-{las}@{domain}')
    emails.append(f'{fir}_{las}@{domain}')

    emails.append(f'{fi}{la}@{domain}')
    emails.append(f'{fi}.{la}@{domain}')
    emails.append(f'{fi}-{la}@{domain}')
    emails.append(f'{fi}_{la}@{domain}')

    ## Adding year 
    emails.append(f'{first}{er}@{domain}')
    emails.append(f'{first}.{er}@{domain}')
    emails.append(f'{first}-{er}@{domain}')
    emails.append(f'{first}_{er}@{domain}')

    emails.append(f'{first}{last}{er}@{domain}')
    emails.append(f'{first}.{last}.{er}@{domain}')
    emails.append(f'{first}-{last}-{er}@{domain}')
    emails.append(f'{first}_{last}_{er}@{domain}')

    emails.append(f'{last}{er}@{domain}')
    emails.append(f'{last}.{er}@{domain}')
    emails.append(f'{last}-{er}@{domain}')
    emails.append(f'{last}_{er}@{domain}')

    emails.append(f'{f}{last}{er}@{domain}')
    emails.append(f'{f}.{last}.{er}@{domain}')
    emails.append(f'{f}-{last}-{er}@{domain}')
    emails.append(f'{f}_{last}_{er}@{domain}')

    emails.append(f'{first}{l}{er}@{domain}')
    emails.append(f'{first}.{l}.{er}@{domain}')
    emails.append(f'{first}-{l}-{er}@{domain}')
    emails.append(f'{first}_{l}_{er}@{domain}')

    emails.append(f'{last}{f}{er}@{domain}')
    emails.append(f'{last}.{f}.{er}@{domain}')
    emails.append(f'{last}-{f}-{er}@{domain}')
    emails.append(f'{last}_{f}_{er}@{domain}')

    emails.append(f'{fir}{las}{er}@{domain}')
    emails.append(f'{fir}.{las}.{er}@{domain}')
    emails.append(f'{fir}-{las}-{er}@{domain}')
    emails.append(f'{fir}_{las}_{er}@{domain}')

    emails.append(f'{fi}{la}{er}@{domain}')
    emails.append(f'{fi}.{la}.{er}@{domain}')
    emails.append(f'{fi}-{la}-{er}@{domain}')
    emails.append(f'{fi}_{la}_{er}@{domain}')
    return emails
