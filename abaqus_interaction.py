import subprocess

abaqus_path = 'D:\\software\\SIMULIA\\Abaqus\\Commands\\abq6144.bat'

def run_cae():
    # Use a breakpoint in the code line below to debug your script.
    process = subprocess.Popen([abaqus_path, 'cae', 'noGUI=./script.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # 实时输出子进程的输出
    for line in iter(process.stdout.readline, b''):
        print(line.decode('utf-8'), end='')
    # 等待子进程完成
    process.communicate()

def verification():
    #    验证参数
    #    SUMMARY: verify executes the Abaqus installation verification
    #             procedure for one or more desired products.
    #      USAGE: abq6141 verify <options> [-log]
    #    OPTIONS: All options may be abbreviated with the shortest string
    #             that is unique. At least one option must be present.
    #    Common Options:
    #             -all         Run all product verification procedures
    #             -help        Display verification usage
    #             -install     Run installation verification procedures
    #             -log         Redirect verification output to a file named
    #                          "verify.log" in the current directory
    #    Product Options:
    #             -ams         Abaqus/AMS verification
    #             -tosca       Tosca For Abaqus verification
    #             -cae         Abaqus/CAE verification
    #             -cfd         Abaqus/CFD verification
    #             -design      Abaqus/Design verification
    #             -exp         Abaqus/Explicit verification
    #             -foundation  Abaqus/Foundation verification
    #             -param       Abaqus/Standard and Abaqus/Explicit parametric
    #                          studies verification
    #             -std         Abaqus/Standard verification
    #             -user_exp    Abaqus/Explicit with user subroutines verification
    #             -user_std    Abaqus/Standard with user subroutines verification
    #             -viewer      Abaqus/Viewer verification
    #    Translator Options:
    #             -adams       Abaqus Interface for MSC.ADAMS verification
    #             -catiav4     Geometry Translator for CATIA V4 verification
    #             -catiav5     Geometry Translator for CATIA V5 verification
    #             -dcatiav5    Verify Direct Geometry Import for CATIA V5 (verifies
    #                          geometry import capability in Abaqus/CAE; does not
    #                          verify installation or functionality of the CATIA V5
    #                          Associative Interface plug-in)
    #             -moldflow    Abaqus Interface for Moldflow verification
    #             -parasolid   Geometry Translator for Parasolid verification
    #             -proe        Verify Geometry Translator for Pro/ENGINEER (verifies
    #                          geometry import capability in Abaqus/CAE; does not
    #                          verify installation or functionality of the
    #                          Pro/ENGINEER Associative Interface plug-in)
    #             -swi         Verify Geometry Translator for SolidWorks (verifies
    #                          geometry import capability in Abaqus/CAE; does not
    #                          verify installation or functionality of the SolidWorks
    #                          Associative Interface plug-in)
    #     Additional Options:
    #             -contextHelp    Abaqus/CAE context-sensitive help verification
    #             -cPerf          Abaqus/CAE performance
    #             -docUrl         Abaqus Documentation verification
    #             -ioPerf         Abaqus I/O performance
    #             -make           Abaqus make utility verification
    #             -noGui          Abaqus noGUI (CAE/Viewer) verification
    #             -NoLicenseCheck Skips all license checks
    #             -parallel       Abaqus analyses using parallelization verification
    #             -scripting      Abaqus scripting interface verification
    #             -verbose        Display debugging information
    #             -retainFiles    Retain verification files
    #      NOTES: If the -install option is used, no other options are permitted.
    result = subprocess.Popen([abaqus_path, '-verify', '-param', '-std', '-user_std'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = result.communicate()
    verification_results = stdout.decode('utf-8')
    # 检查是否存在错误或者警告
    substring = 'PASS'
    if verification_results.count(substring) == 4:
        print('程序验证成功')
    else:
        print('程序验证失败')