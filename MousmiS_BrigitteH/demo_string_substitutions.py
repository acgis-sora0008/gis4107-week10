#-------------------------------------------------------------------------------
# Name:        demo_string_templates.py
# Purpose:     Demonstrate how the string.Template class works + other string
#              formatting options.
# Author:      David Viljoen
# Created:     09/11/2021
#-------------------------------------------------------------------------------

from string import Template

def main():
    # The string.Template class supports $-substitutions.  The $ delimiter can
    # be replaced with another character.  The Template class takes a template
    # as an argument.  A template is a string with substitution identifiers
    # e.g. $identifier If there is no space after the text to be substituted,
    # use { }, e.g. ${identifier}no_space_after_identifier
    #
    # Values to be used in the substitution can be from a dictionary.

    print( "Using string.Template ...")
    template = "My name is $name.  ${activity}ing is good for you.\n"
    t = Template(template)

    d = {"name": "David", "activity": "Bik"}
    print( t.substitute(d))

    print( "Using .format() ...")
    
    fmt = "My name is {name}.  {activity}ing is good for you\n"

    print( fmt.format(name="David", activity="Bik"))

    print(  "Using ** operator ...")
    
    print( fmt.format(**d))

    print( "Passing keyword args demo ...")
    unpack_kwargs(name="David", activity="Bike")

    print('\nUsing f-strings')
    name="David"
    activity="Bike"
    print(f"""Name: {name}
Activity: {activity}""")

def unpack_kwargs(**kwargs):
    print( "\nUnpacking kwargs ...")
    print( "key: value")
    print( "---: -----")
    for key in kwargs.keys():
        print( "{}: {}".format(key, kwargs[key]))

if __name__ == '__main__':
    main()
